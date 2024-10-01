import streamlit as st
from database_manager import DatabaseManager  # Assurez-vous d'avoir le bon chemin d'importation
from Utilisateurs import gestion_utilisateurs  # Importer la fonction de gestion des utilisateurs
from Produit import gestion_produits # Importer la fonction de gestion des produits

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
    gestion_produits()

# Page de gestion des utilisateurs
elif page == "Gestion des Utilisateurs":
    gestion_utilisateurs()  # Appel de la fonction pour gérer les utilisateurs

# Fermer la connexion à la base de données à la fin
db.close_connection()
