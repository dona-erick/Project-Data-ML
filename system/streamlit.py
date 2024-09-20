import streamlit as st
from gensim.models import Word2Vec
import gensim
import pandas as pd

import streamlit as st
from recommend import recommender_extended

# Interface utilisateur pour entrer le nom de l'artiste
artist_name = st.text_input("Entrez le nom de l'artiste :")

# Bouton pour générer les recommandations
if st.button("Recommander des chansons similaires"):
    if artist_name:
        # Utiliser la fonction de recommandation
        recommended_songs = recommender_extended(artist_name)
        st.write("Chansons similaires :")
    else:
        st.write("Veuillez entrer un nom d'artiste.")
