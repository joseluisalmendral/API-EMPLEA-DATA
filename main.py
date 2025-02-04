from bson import ObjectId
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from config import DB_COLLECTION, DB_PASS, DB_NAME
import pandas as pd

# Configurar la conexión con MongoDB Atlas
MONGO_URI = f"mongodb+srv://root:{DB_PASS}@cluster0.pse9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Conectar con la base de datos
client = MongoClient(MONGO_URI)

try:
    client.admin.command("ping")
    print("✅ Conexión realizada con éxito!")
except Exception as e:
    print("❌ Error en la conexión a MongoDB:", e)

# Seleccionar base de datos y colección
db = client[DB_NAME]
collection = db[DB_COLLECTION]

# Crear la API con FastAPI
app = FastAPI()

# Función para serializar ObjectId
def serialize_document(document):
    if not document:
        return None
    document["_id"] = str(document["_id"])  # Convierte ObjectId a string
    return document

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}

@app.get("/debug")
def debug_data():
    try:
        # Recuperar los primeros 5 documentos para depuración
        sample_data = [serialize_document(doc) for doc in collection.find().limit(5)]
        return {"sample_data": sample_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/check-fields")
def check_fields():
    try:
        # Extraer un documento para inspección
        sample_document = collection.find_one()
        serialized_document = serialize_document(sample_document)
        return {"sample_document": serialized_document}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get-top-skills")
def get_top_skills():
    try:
        # Definir el pipeline de agregación en MongoDB
        pipeline = [
            {"$unwind": "$Skills"},
            {"$group": {"_id": "$Skills", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 15}
        ]

        # Ejecutar la consulta y convertir a DataFrame
        skills = list(collection.aggregate(pipeline))

        # Verificar si la consulta devolvió resultados
        if not skills:
            return {"message": "No se encontraron datos en la colección para el campo 'Skills'"}

        # Convertir los resultados en un DataFrame y serializar los IDs
        df_skills = pd.DataFrame(skills)
        df_skills["_id"] = df_skills["_id"].apply(str)  # Convierte ObjectId a string

        # Renombrar columnas
        df_skills.columns = ["Skill", "Frecuencia"]

        # Convertir a JSON
        top_skills_json = [{"skill": row["Skill"], "count": row["Frecuencia"]} for _, row in df_skills.iterrows()]

        return {"top_skills": top_skills_json}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
