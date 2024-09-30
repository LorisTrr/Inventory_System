import streamlit as st
from datetime import datetime
from database_manager import DatabaseManager  # Importez la classe DatabaseManager

def gestion_utilisateurs():
   # Configuration de la connexion à la base de données
    db_manager = DatabaseManager(
        host_name='localhost',           # Utiliser 'host_name' au lieu de 'host'
        user_name='root',               # Utiliser 'user_name'
        user_password='',                # Utiliser 'user_password'
        db_name='inventiry_system'       # Utiliser 'db_name'
    )

    st.title("Gestion des Utilisateurs")

    # Formulaire d'ajout d'utilisateur
    nom = st.text_input("Veuillez entrer votre nom :")
    prenom = st.text_input("Veuillez entrer votre prénom :")
    email = st.text_input("Veuillez entrer votre email :")
    telephone = st.text_input("Veuillez entrer votre numéro de téléphone :")
    mot_de_passe = st.text_input("Veuillez entrer votre mot de passe :", type='password')
    est_admin = st.checkbox("Est-ce un administrateur ?")

    if st.button("Ajouter Utilisateur"):
        date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db_manager.add_user(nom, prenom, email, telephone, mot_de_passe, est_admin, date_creation)  # Ajouter l'utilisateur
        st.success(f"Utilisateur '{nom} {prenom}' ajouté avec succès.")

    # Afficher les utilisateurs existants
    st.subheader("Utilisateurs Existants")
    utilisateurs = db_manager.get_users()
    
    if utilisateurs:
        for utilisateur in utilisateurs:
            st.write(f"Nom: {utilisateur[1]}, Prénom: {utilisateur[2]}, Email: {utilisateur[3]}, Téléphone: {utilisateur[4]}, Admin: {utilisateur[6]}, Date de création: {utilisateur[7]}")
    else:
        st.warning("Aucun utilisateur trouvé.")

    # Fermer la connexion à la base de données à la fin
    db_manager.close_connection()

# Si tu souhaites exécuter ce fichier indépendamment, tu peux ajouter cette condition
if __name__ == "__main__":
    gestion_utilisateurs()
