import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Definir variables de configuración
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")

# Validar que las variables de entorno existan
if not DB_PASS or not DB_NAME or not DB_COLLECTION:
    raise ValueError("Faltan variables de entorno requeridas: DB_PASS, DB_NAME o DB_COLLECTION")
