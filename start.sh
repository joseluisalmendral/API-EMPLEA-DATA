export $(grep -v '^#' .env | xargs)  # Cargar variables de entorno (por si acaso)
uvicorn main:app --host 0.0.0.0 --port $PORT