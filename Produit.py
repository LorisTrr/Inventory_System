import streamlit as st
from database_manager import DatabaseManager
import csv
import io
import plotly.graph_objects as go

# Fonction pour charger et appliquer le CSS externe
def charger_css(fichier_css):
    with open(fichier_css) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def export_to_csv(db_manager):
    try:
        # Exécution de la requête
        data = db_manager.get_products()

        # Récupération des noms de colonnes
        headers = ['ID', ' Nom', ' Prix', ' Quantité',' Date de création du fichier']

        # Création du fichier CSV en mémoire
        output = io.StringIO()
        csv_writer = csv.writer(output)
        csv_writer.writerow(headers)  # Écriture des en-têtes
        csv_writer.writerows(data)    # Écriture des données

        return output.getvalue()

    except Exception as error:
        st.error(f"Erreur lors de l'exportation des données : {error}")
        return None

def afficher_graphe_quantites(db_manager):
    products = db_manager.get_products()
    
    if products:
        noms = [produit[1] for produit in products]
        quantites = [produit[3] for produit in products]
        
        fig = go.Figure(data=[go.Bar(x=noms, y=quantites)])
        
        fig.update_layout(
            title="Quantités par produit",
            xaxis_title="Produits",
            yaxis_title="Quantité en stock",
            bargap=0.2
        )
        
        st.plotly_chart(fig)
    else:
        st.warning("Aucun produit trouvé pour générer le graphe.")



def gestion_produits():
    # Charger le fichier CSS
    charger_css("produit.css")

    # Configuration de la connexion à la base de données
    db_manager = DatabaseManager(
        host_name='localhost',
        user_name='root',
        user_password='',
        db_name='inventory'
    )
    # Page de gestion des produits
    st.title("Système de Gestion d'Inventaire - Produits")
    
    # Ajouter un produit
    st.subheader("Ajouter un nouveau produit")
    nom = st.text_input("Nom du produit")
    prix = st.number_input("Prix", min_value=0.00, format="%.2f")
    quantite = st.number_input("Quantité", min_value=0)

    if st.button("Ajouter produit"):
        if nom and prix > 0 and quantite > 0:
            db_manager.add_product(nom, prix, quantite)
            st.success("Produit ajouté avec succès !")
        else:
            st.error("Veuillez remplir tous les champs correctement.")

    # Afficher les produits disponibles
    st.subheader("Produits Disponibles")
    produits = db_manager.get_products()

    # Afficher les produits dans un tableau
    if produits:
        for produit in produits:
            product_id = produit[0]  # L'ID du produit est à l'index 0 dans chaque ligne

            st.markdown(f"""
                        <div class="produits-card">
                            <div class="produits-info">
                                <h3>{produit[1]}</h3> <!-- Nom du produit -->
                                <p>ID: {produit[0]}</p> <!-- ID du produit -->
                                <p>Prix: {produit[2]:.2f} €</p> <!-- Prix du produit -->
                                <p>Quantité: {produit[3]}</p> <!-- Quantité disponible -->
                            </div>
                        </div>
            """, unsafe_allow_html=True)

            # Bouton Streamlit pour la suppression, avec une clé unique pour chaque produit
            if st.button(f"Supprimer {produit[1]}"):
                db_manager.delete_product(product_id)
                st.success(f"Produit '{produit[1]}' supprimé avec succès.")
                
         # Bouton pour afficher le graphe
        if st.button("Afficher le graphique des quantités"):
            st.subheader("Graphique des quantités en stock")
            afficher_graphe_quantites(db_manager)
            
            
            # Bouton pour générer le CSV
        if st.button("Générer CSV"):
            csv_data = export_to_csv(db_manager)
            if csv_data:
                st.download_button(
                    label="Télécharger CSV",
                    data=csv_data,
                    file_name="produits.csv",
                    mime="text/csv"
                )
                st.success("Fichier CSV généré avec succès !")
            else:
                st.error("Erreur lors de la génération du fichier CSV.")
    else:
        st.warning("Aucun produit trouvé.")

    # Fermer la connexion à la base de données à la fin
    db_manager.close_connection()

