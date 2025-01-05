from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

DATA_FILE = "cars.json"

#Modelos:
class Cars(BaseModel):
    id: int;
    model: str;
    available: bool;

class Reservas(BaseModel):
    car_id: int;
    date: str;
    
# Cargar datos iniciales o crear archivo si no existe
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(DATA_FILE, "w") as file:
            json.dump({"cars": [], "bookings": []}, file)
        return {"cars": [], "bookings": []}
    
# Guardar datos, en este caso usaremos el json para guardar los datos para hacerlo mas rapido, lo suyo seria tenerlo junto a una base de datos.
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

