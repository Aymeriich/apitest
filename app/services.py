import json
from datetime import date

DATA_FILE = "cars.json"

# Datos que se crearán si no existe el archivo
def initialize_data():
    try:
        with open(DATA_FILE, "r") as file:
            json.load(file)
    except FileNotFoundError:
        default_data = {
            "cars": [
                {"id": 1, "model": "Toyota Corolla", "available": True},
                {"id": 2, "model": "Honda Civic", "available": True},
                {"id": 3, "model": "Ford Focus", "available": True},
                {"id": 4, "model": "Hyundai Elantra", "available": True},
                {"id": 5, "model": "Chevrolet Cruze", "available": True}
            ],
            "bookings": []
        }
        with open(DATA_FILE, "w") as file:
            json.dump(default_data, file)

initialize_data()

def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_reserved_cars(for_date: date):
    data = load_data()
    reserved_cars = {b["car_id"] for b in data["bookings"] if b["date"] == for_date.isoformat()}
    return reserved_cars
