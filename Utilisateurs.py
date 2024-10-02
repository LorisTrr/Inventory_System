import streamlit as st
from datetime import datetime
from database_manager import DatabaseManager

# Fonction pour charger et appliquer le CSS externe
def charger_css(fichier_css):
    with open(fichier_css) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def gestion_utilisateurs():
    # Charger le fichier CSS
    charger_css("users.css")

    # Configuration de la connexion à la base de données
    db_manager = DatabaseManager(
        host_name='localhost',
        user_name='root',
        user_password='',
        db_name='inventory_system'
    )

    st.title("Gestion des Utilisateurs")

    # Formulaire d'ajout d'utilisateur
    nom = st.text_input("Veuillez entrer votre nom :")
    prenom = st.text_input("Veuillez entrer votre prénom :")
    email = st.text_input("Veuillez entrer votre email :")
    telephone = st.text_input("Veuillez entrer votre numéro de téléphone :")
    mot_de_passe = st.text_input("Veuillez entrer votre mot de passe :", type='password')
    est_admin = st.checkbox("Est-ce un administrateur ?")

    # Vérifier si le bouton d'ajout est cliqué
    if st.button("Ajouter Utilisateur"):
        # Vérifier si tous les champs obligatoires sont remplis
        if not nom or not prenom or not email or not telephone or not mot_de_passe:
            st.error("Tous les champs sont obligatoires. Veuillez remplir toutes les informations avant d'ajouter un utilisateur.")
        else:
            # Ajouter l'utilisateur si tout est rempli
            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db_manager.add_user(nom, prenom, email, telephone, mot_de_passe, est_admin, date_creation)
            st.success(f"Utilisateur '{nom} {prenom}' ajouté avec succès.")

    # Afficher les utilisateurs existants
    st.subheader("Utilisateurs Existants")
    utilisateurs = db_manager.get_users()

    if utilisateurs:
        for utilisateur in utilisateurs:
            user_id = utilisateur[0]  # Supposons que l'ID de l'utilisateur est à l'index 0
            st.markdown(f"""
                <div class="utilisateur-card">
                    <div class="utilisateur-info">
                        <h3>{utilisateur[1]} {utilisateur[2]}</h3>
                        <p>Email: {utilisateur[3]}</p>
                        <p>Téléphone: {utilisateur[4]}</p>
                        <p>Admin: {'Oui' if utilisateur[6] else 'Non'}</p>
                        <p>Date de création: {utilisateur[7]}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Utiliser un bouton Streamlit pour la suppression
            if st.button(f"Supprimer {utilisateur[1]} {utilisateur[2]}"):
                db_manager.delete_user(user_id)
                st.success(f"Utilisateur '{utilisateur[1]} {utilisateur[2]}' supprimé avec succès.")
    else:
        st.warning("Aucun utilisateur trouvé.")

    # Fermer la connexion à la base de données à la fin
    db_manager.close_connection()