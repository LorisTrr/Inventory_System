import streamlit as st
from database_manager import DatabaseManager

# Fonction pour charger et appliquer le CSS externe
def charger_css(fichier_css):
    with open(fichier_css) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def gestion_produits():
    # Charger le fichier CSS
    charger_css("produit.css")

    # Configuration de la connexion à la base de données
    db_manager = DatabaseManager(
        host_name='localhost',
        user_name='root',
        user_password='',
        db_name='inventiry_system'
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
            st.markdown(f"""
                        <div class="produits-card">
                            <div class="produits-info">
                                <h3>{produit[1]}</h3>
                                <p>ID: {produit[0]}</p>
                                <p>Prix: {produit[2]}</p>
                                <p>Quantité: {produit[3]}</p>
                            </div>
                        </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Aucun produit trouvé.")