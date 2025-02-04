import os

# Intentar obtener las variables de entorno usando os.environ.get
DB_PASS = os.environ.get("DB_PASS", "MISSING")
DB_NAME = os.environ.get("DB_NAME", "MISSING")
DB_COLLECTION = os.environ.get("DB_COLLECTION", "MISSING")

# Imprimir las variables para depuración
print(f"🔍 DEBUG xxx: DB_PASS={DB_PASS}, DB_NAME={DB_NAME}, DB_COLLECTION={DB_COLLECTION}")

# Validar que las variables de entorno existan
# if "MISSING" in [DB_PASS, DB_NAME, DB_COLLECTION]:
#     raise ValueError("❌ ERROR: Faltan variables de entorno requeridas en Render")
