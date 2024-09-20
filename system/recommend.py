import gensim
from gensim.models import Word2Vec
import pandas as pd
# Fonction de recommandation qui inclut chansons, playlists et albums
model = Word2Vec.load('/home/einstein/NLP/system/recommended.model')
data = pd.read_csv('/home/einstein/NLP/system/data.csv')
def recommender_extended(Name_artist, top_n=10):
    try:
        # Trouver les chansons similaires
        similar_songs = model.wv.most_similar(Name_artist, topn=top_n)
        
        # Afficher les recommandations de chansons
        print(f"Chansons similaires pour l'artiste '{Name_artist}':")
    
    except KeyError:
        print(f"L'artiste '{Name_artist}' n'est pas dans le modèle.")
