import streamlit as st
import re  # Bibliothèque pour les expressions régulières
from datetime import datetime
from database_manager import DatabaseManager

# Fonction pour charger et appliquer le CSS externe
def charger_css(fichier_css):
    with open(fichier_css) as f:
        # Utilisation de Streamlit pour insérer du CSS personnalisé
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Fonction pour valider l'email
def valider_email(email):
    # Expression régulière pour valider un email standard (format exemple@exemple.com)
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # Vérifie si l'email correspond au modèle
    return re.match(email_regex, email) is not None

# Fonction pour valider le numéro de téléphone français
def valider_numero_telephone(telephone):
    # Expression régulière pour vérifier que le numéro de téléphone est un numéro français
    # Il doit commencer par 0 et être suivi de 9 autres chiffres
    telephone_regex = r'^0[1-9]\d{8}$'
    # Vérifie si le numéro correspond au modèle
    return re.match(telephone_regex, telephone) is not None

# Fonction pour valider le mot de passe
def valider_mot_de_passe(mot_de_passe):
    # Vérifie si le mot de passe a au moins 8 caractères
    if len(mot_de_passe) < 8:
        return False
    # Vérifie la présence d'au moins une majuscule
    if not re.search(r'[A-Z]', mot_de_passe):
        return False
    # Vérifie la présence d'au moins une minuscule
    if not re.search(r'[a-z]', mot_de_passe):
        return False
    # Vérifie la présence d'au moins un chiffre
    if not re.search(r'\d', mot_de_passe):
        return False
    # Si toutes les conditions sont respectées, le mot de passe est valide
    return True

def gestion_utilisateurs():
    # Charger le fichier CSS externe pour styliser l'interface
    charger_css("users.css")

    # Configuration de la connexion à la base de données
    db_manager = DatabaseManager(
        host_name='localhost',  # Adresse du serveur MySQL
        user_name='root',  # Nom d'utilisateur MySQL
        user_password='',  # Mot de passe MySQL (vide dans ce cas)
        db_name='inventory'  # Nom de la base de données
    )

    st.title("Gestion des Utilisateurs")

    # Création du formulaire pour saisir les informations utilisateur
    nom = st.text_input("Veuillez entrer votre nom :")
    prenom = st.text_input("Veuillez entrer votre prénom :")
    email = st.text_input("Veuillez entrer votre email :")
    telephone = st.text_input("Veuillez entrer votre numéro de téléphone :")
    mot_de_passe = st.text_input("Veuillez entrer votre mot de passe :", type='password')
    est_admin = st.checkbox("Est-ce un administrateur ?")

    # Vérification si le bouton "Ajouter Utilisateur" a été cliqué
    if st.button("Ajouter Utilisateur"):
        # Vérifie que tous les champs obligatoires sont remplis
        if not nom or not prenom or not email or not telephone or not mot_de_passe:
            st.error("Tous les champs sont obligatoires. Veuillez remplir toutes les informations avant d'ajouter un utilisateur.")
        else:
            # Validation de l'email
            if not valider_email(email):
                st.error("L'email n'est pas valide. Veuillez entrer un email au format exemple@exemple.com.")
            # Validation du numéro de téléphone français
            elif not valider_numero_telephone(telephone):
                st.error("Le numéro de téléphone doit être un numéro français valide (10 chiffres, commençant par 0).")
            # Validation du mot de passe
            elif not valider_mot_de_passe(mot_de_passe):
                st.error("Le mot de passe doit contenir au moins 8 caractères, une majuscule, une minuscule et un chiffre.")
            else:
                # Si toutes les validations sont correctes, on peut ajouter l'utilisateur à la base de données
                date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Enregistre la date et l'heure actuelle
                db_manager.add_user(nom, prenom, email, telephone, mot_de_passe, est_admin, date_creation)
                st.success(f"Utilisateur '{nom} {prenom}' ajouté avec succès.")  # Message de succès

    # Section pour afficher les utilisateurs existants
    st.subheader("Utilisateurs Existants")
    utilisateurs = db_manager.get_users()

    if utilisateurs:
        # Afficher les informations de chaque utilisateur dans la base de données
        for utilisateur in utilisateurs:
            user_id = utilisateur[0]  # ID de l'utilisateur
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

            # Bouton pour supprimer un utilisateur
            if st.button(f"Supprimer {utilisateur[1]} {utilisateur[2]}"):
                db_manager.delete_user(user_id)  # Supprimer l'utilisateur de la base de données
                st.success(f"Utilisateur '{utilisateur[1]} {utilisateur[2]}' supprimé avec succès.")
    else:
        st.warning("Aucun utilisateur trouvé.")  # Message si aucun utilisateur n'est présent

    # Fermeture de la connexion à la base de données
    db_manager.close_connection()