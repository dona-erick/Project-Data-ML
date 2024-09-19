from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib
import datetime
app = FastAPI()

### chargement du model
model = joblib.load('/home/einstein/Projects Data Science/British_vol/backend/model_vol/pipeline_model_bagging.joblib')
## creation d'un classe reservation
class Reservation(BaseModel):
    nom: str
    prenom: str
    email: str
    nationality: str
    origine: str
    #birth_date: SkipValidation[datetime]
    profession: str
    trip_voyage: str
    duree_sejour: int
    hour_vol: int
    flight_duration: float
    booking_channel: str
    destination : str
    bags_extra : bool
    day_passed : int
    
    #class Config:
     #   arbitrary_types_allowed = True
    
reservations = []
    
## endpoint
@app.post("/reserve")
def create_reservation(reservation: Reservation):
    try:
        reservations.append(reservation)
   
        return {
            "message": "Votre Réservation a été pris en compte avec succès! Merci, un retour vous sera fait par mail", 
            'reservation': reservation
            }
    except Exception as e:
        return {"error": "Nous sommes désolés. Veuillez ressayer plus tard !",
                "detail": str(e)
        }

## prediction 

class PredictionReserve(BaseModel):
    num_passengers: int
    sales_channel:str
    trip_type:str
    purchase_lead:int
    length_of_stay:int
    flight_hour: int
    #flight_day:str
    #route:str
    #booking_origin: str
    wants_extra_baggage: int
    wants_preferred_seat: int
    wants_in_flight_meals: int
    flight_duration: float
    #booking_complete: int
    
@app.post('/predict')
def prediction_reserve(data: PredictionReserve):
    try:
        
        input_data = [[
            data.num_passengers,
            1 if data.sales_channel == 'internet' else 0,
            1 if data.trip_type == 'CircleTrip' else 0,
            data.purchase_lead,
            data.length_of_stay,
            data.flight_hour,
            #data.flight_day,
            #data.route,
            #data.booking_origin,
            data.wants_extra_baggage,
            data.wants_preferred_seat,
            data.wants_in_flight_meals,
            data.flight_duration
            ]]
        ##predire si le vol sera rsevé
        prediction = model.predict(input_data)
        
        return {"Prediction": "Le vol sera reservé" 
                if prediction[0] == 1 else "Le vol ne sera pas reservé"
                }
    except Exception as e:
        raise HTTPException(status_code=400, detail= str(e))
    
        
    