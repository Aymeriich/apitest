from fastapi import APIRouter, HTTPException
from datetime import date
from app.models import Car, Booking
from app.services import load_data, save_data, get_reserved_cars
import logging

router = APIRouter()

# Listar vehículos disponibles
@router.get("/cars", response_model=list[Car])
def get_cars(for_date: date):
    data = load_data()
    reserved_cars = get_reserved_cars(for_date)
    available_cars = [Car(**car) for car in data["cars"] if car["available"] and car["id"] not in reserved_cars]
    
    logging.info(f"Queried available cars for date {for_date}.")
    return available_cars

# Crear una reserva
@router.post("/bookings")
def create_booking(booking: Booking):
    data = load_data()

    # Verificar si el auto existe
    if booking.car_id not in {car["id"] for car in data["cars"]}:
        logging.error(f"Car {booking.car_id} not found")
        raise HTTPException(status_code=404, detail="Car not found")

    # Validar que la fecha no sea en el pasado
    if booking.date < date.today():
        logging.error(f"Cannot book in the past {booking.date}")
        raise HTTPException(status_code=400, detail="Cannot book in the past")

    # Validar si el auto ya está reservado en la misma fecha
    if any(b["car_id"] == booking.car_id and b["date"] == booking.date.isoformat() for b in data["bookings"]):
        logging.error(f"Car {booking.car_id} already booked on {booking.date}")
        raise HTTPException(status_code=400, detail="Car already booked on this date")

    # Registrar la reserva
    data["bookings"].append({"car_id": booking.car_id, "date": booking.date.isoformat()})
    save_data(data)
    logging.info(f"Booking created for car {booking.car_id} on {booking.date}")
    return {"message": "Booking created successfully"}
