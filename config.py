import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")
