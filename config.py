import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Definir variables de configuración
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")

# Validar que las variables de entorno existan
missing_vars = [var for var in ["DB_PASS", "DB_NAME", "DB_COLLECTION"] if not locals()[var]]

if missing_vars:
    print(f"⚠️ Advertencia: Faltan variables de entorno: {', '.join(missing_vars)}")
else:
    print("✅ Variables de entorno cargadas correctamente")