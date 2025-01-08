from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que la app se importe correctamente

"""
En caso de que no se importe correctamente abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando:
set PYTHONPATH=.
"""

client = TestClient(app)

def test_get_cars():
    response = client.get("/cars", params={"for_date": "2025-01-10"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_booking():
    response = client.post("/bookings", json={"car_id": 1, "date": "2025-01-10"})
    assert response.status_code == 200
    assert response.json()["message"] == "Booking created successfully"

def test_booking_past_date():
    response = client.post("/bookings", json={"car_id": 1, "date": "2020-01-10"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot book in the past"
    
def test_booking_non_existent_car():
    response = client.post("/bookings", json={"car_id": 99, "date": "2025-01-10"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found"
    
def test_booking_already_reserved():
    response = client.post("/bookings", json={"car_id": 1, "date": "2025-01-10"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Car already booked on this date"