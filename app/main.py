from fastapi import FastAPI
from app.endpoints import router
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/API-logs.log"),  # Guardar en el directorio logs
        logging.StreamHandler()
    ]
)

app = FastAPI()

# Incluir los endpoints en la aplicación
app.include_router(router)
