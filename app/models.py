from pydantic import BaseModel
from datetime import date

class Car(BaseModel):
    id: int
    model: str
    available: bool

class Booking(BaseModel):
    car_id: int
    date: date
