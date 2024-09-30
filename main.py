import streamlit as st
from database_manager import DatabaseManager  # Assurez-vous d'avoir le bon chemin d'importation
from Utilisateurs import gestion_utilisateurs  # Importer la fonction de gestion des utilisateurs

# Configuration de la connexion à la base de données
db = DatabaseManager(
    host_name='localhost',           # Utiliser 'host_name' au lieu de 'host'
    user_name='root',               # Utiliser 'user_name'
    user_password='',                # Utiliser 'user_password'
    db_name='inventiry_system'       # Utiliser 'db_name'
)
# Ajout de la barre latérale pour la navigation
page = st.sidebar.selectbox("Choisissez la page", ["Gestion des Produits", "Gestion des Utilisateurs"])

# Page de gestion des produits
if page == "Gestion des Produits":
    st.title("Système de Gestion d'Inventaire - Produits")

    # Afficher les produits disponibles
    st.subheader("Produits Disponibles")
    produits = db.get_products()

    # Afficher les produits dans un tableau
    if produits:
        for produit in produits:
            st.write(f"ID: {produit[0]}, Nom: {produit[1]}, Prix: {produit[2]}, Quantité: {produit[3]}")
    else:
        st.write("Aucun produit trouvé.")

    # Ajouter un produit
    st.subheader("Ajouter un nouveau produit")
    nom = st.text_input("Nom du produit")
    prix = st.number_input("Prix", min_value=0.00, format="%.2f")
    quantite = st.number_input("Quantité", min_value=0)

    if st.button("Ajouter produit"):
        if nom and prix > 0 and quantite > 0:
            db.add_product(nom, prix, quantite)
            st.success("Produit ajouté avec succès !")
        else:
            st.error("Veuillez remplir tous les champs correctement.")

# Page de gestion des utilisateurs
elif page == "Gestion des Utilisateurs":
    gestion_utilisateurs()  # Appel de la fonction pour gérer les utilisateurs

# Fermer la connexion à la base de données à la fin
db.close_connection()
