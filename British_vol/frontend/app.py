import streamlit as st
import joblib
import requests

##url du backend 
url = "http://127.0.0.1:8000"

st.title("Booked Tripe here")

## formulaire pour créer une reservation
with st.form('Reservation de Voyage'):
    nom = st.text_input('Entrez votre nom')
    prenom= st.text_input('Entrez votre prenom')
    email= st.text_input('Entrez votre email')
    nationality= st.selectbox('nationality', ['Beninoise', 'Togolaise', 'Nigerienne', "Amerique"])
    origine = st.selectbox('origine', ["Porto-Novo", 'Kandi', 'Ouidah'])
    #birth_date: SkipValidation[datetime]
    profession= st.text_input('Profession')
    trip_voyage= st.selectbox('Voyage', ['CircleTrip', "OneWay", "RoundTrip"])
    duree_sejour= st.number_input('Nombre de séjour')
    hour_vol= st.number_input('heure de vol')
    flight_duration= st.number_input('Durée de vol')
    booking_channel= st.selectbox('Canal Reservation', ["internet", 'mobile'])
    destination = st.text_input('Destination')
    bags_extra = st.checkbox('Baggage Supplémentaire')
    day_passed = st.number_input('Nombre de jour à passer')
    
    submit = st.form_submit_button("Reserver")
    if submit:
        reservation = {
            "nom": nom,
            "prenom": prenom,
            "email": email,
            "nationality": nationality,
            "origine": origine,
            #birth_date: SkipValidation[datetime]
            "profession": profession,
            "trip_voyage": trip_voyage,
            "duree_sejour": duree_sejour,
            "hour_vol": hour_vol,
            "flight_duration": flight_duration,
            "booking_channel": booking_channel,
            "destination" : destination,
            "bags_extra" : bags_extra,
            "day_passed" : day_passed
        }
        response = requests.post(f"{url}/predict", json=reservation)
        
        if response.status_code == 200:
            result = response.json()
            prediction = result.get('prediction', 'Aucune prédiction disponible')
            st.write(f"Prédiction : {prediction}")
        else:
            st.write("Erreur lors de la prédiction. Veuillez réessayer.")

        # Envoyer la réservation pour la créer
        response = requests.post(f"{url}/reserve", json=reservation)
        
        if response.status_code == 200:
            result = response.json()
            message = result.get('message', 'Aucune confirmation disponible')
            st.write(message)
        else:
            st.write("Erreur lors de la création de la réservation. Veuillez réessayer.")