import streamlit as st

# Titre de la page
st.title("Test d'affichage avec Streamlit")

# Sous-titre
st.header("Bienvenue dans mon application Streamlit")

# Texte simple
st.write("Ceci est un test d'affichage. Pas de données pour l'instant !")

# Ajouter un bouton
if st.button("Cliquez ici"):
    st.write("Le bouton a été cliqué !")

# Ajouter un slider
valeur = st.slider("Sélectionnez une valeur", 0, 100)
st.write(f"Valeur sélectionnée : {valeur}")
