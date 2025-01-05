from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("api-test.log"),
        logging.StreamHandler()
    ]
)

app = FastAPI()

DATA_FILE = "cars.json"

#Modelos:
class Cars(BaseModel):
    id: int;
    model: str;
    available: bool;

class Bookings(BaseModel):
    car_id: int;
    date: date;
    
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

# Endpoints
# Listar vehiculos disponibles
@app.get("/cars", response_model=list[Cars])
def get_cars(for_date: date):
    data = load_data()
    reserved_cars = {b["car_id"] for b in data["bookings"] if b["date"] == for_date.isoformat()}
    available_cars = [Cars(**car) for car in data["cars"] if car["available"] and car["id"] not in reserved_cars]
    return available_cars

# Crear una reserva
@app.post("/bookings")
def create_booking(booking: Bookings):
    data = load_data()

    # Verificar si el auto existe
    if booking.car_id not in {car["id"] for car in data["cars"]}:
        raise HTTPException(status_code=404, detail="Car not found")
        logging.error(f"Car {booking.car_id} not found")

    # Validar que la fecha no sea en el pasado
    if booking.date < date.today():
        raise HTTPException(status_code=400, detail="Cannot book in the past")
        logging.error(f"Cannot book in the past {booking.date}")

    # Validar si el auto ya está reservado en la misma fecha
    if any(b["car_id"] == booking.car_id and b["date"] == booking.date.isoformat() for b in data["bookings"]):
        raise HTTPException(status_code=400, detail="Car already booked on this date")
        logging.error(f"Car {booking.car_id} already booked on {booking.date}")

    # Registrar la reserva
    data["bookings"].append({"car_id": booking.car_id, "date": booking.date.isoformat()})
    save_data(data)
    logging.info(f"Booking created for car {booking.car_id} on {booking.date}")
    return {"message": "Booking created successfully"}


# Datos que creara en caso de no tener el archivo creado
def initialize_data():
    data = {
        "cars": [
            {"id": 1, "model": "Toyota Corolla", "available": True},
            {"id": 2, "model": "Honda Civic", "available": True},
            {"id": 3, "model": "Ford Focus", "available": True},
            {"id": 4, "model": "Chevrolet Malibu", "available": True},
            {"id": 5, "model": "Nissan Sentra", "available": True}
        ],
        "bookings": []
    }
    save_data(data)

initialize_data()