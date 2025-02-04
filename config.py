import os

# Intentar obtener las variables de entorno usando os.environ.get
DB_COLLECTION = os.environ.get("DB_COLLECTION", "MISSING")
DB_NAME = os.environ.get("DB_NAME", "MISSING")
DB_PASS = os.environ.get("DB_PASS", "MISSING")