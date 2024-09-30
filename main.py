import streamlit as st
from database_manager import DatabaseManager  # Assurez-vous d'avoir le bon chemin d'importation

# Configuration de la connexion à la base de données
db = DatabaseManager(
    host='localhost',
    user='root',          # Remplace par ton nom d'utilisateur MySQL
    password='',          # Remplace par ton mot de passe MySQL
    database='test2'
)

# Interface utilisateur avec Streamlit
st.title("Système de Gestion d'Inventaire")

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
    db.add_product(nom, prix, quantite)
    st.success("Produit ajouté avec succès !")

# Fermer la connexion à la base de données à la fin
db.close_connection()
