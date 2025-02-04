import os

# Intentar obtener las variables de entorno
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")

# Imprimir las variables para depuración (esto se verá en los logs de Render)
print(f"🔍 DEBUG: DB_PASS={DB_PASS}, DB_NAME={DB_NAME}, DB_COLLECTION={DB_COLLECTION}")

# Validar que las variables de entorno existan
if not DB_PASS or not DB_NAME or not DB_COLLECTION:
    raise ValueError("❌ ERROR: Faltan variables de entorno requeridas en Render")
