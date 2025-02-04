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


@app.get("/location-distribution")
def location_distribution():
    """
    Obtiene la distribución de ofertas de empleo por ubicación desde MongoDB.
    Retorna los datos ordenados en JSON.
    """
    try:
        pipeline = [
            { "$group": { "_id": "$Ubicacion", "count": { "$sum": 1 } } },
            { "$sort": { "count": -1 } }
        ]
        results = list(collection.aggregate(pipeline))
        df = pd.DataFrame(results)
        df.columns = ["Ubicación", "Frecuencia"]
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/job-offers-over-time")
def job_offers_over_time():
    """
    Obtiene la evolución de ofertas laborales por categoría a lo largo del tiempo.
    Retorna los datos en formato JSON.
    """
    try:
        pipeline = [
            { "$group": { "_id": { "categoria": "$cat_original", "mes": { "$substr": ["$fecha", 0, 7] } }, "count": { "$sum": 1 } } },
            { "$sort": { "_id.mes": 1 } }
        ]
        results = list(collection.aggregate(pipeline))
        formatted_results = [
            {"Categoría": d["_id"]["categoria"], "Mes": d["_id"]["mes"], "Cantidad de Ofertas": d["count"]}
            for d in results
        ]
        return formatted_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))