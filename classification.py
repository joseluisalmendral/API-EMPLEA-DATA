import unicodedata

# Función para normalizar textos: convierte a minúsculas, elimina espacios laterales y remueve acentos.
def normalizar(texto: str) -> str:
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in texto if not unicodedata.combining(c))

# Diccionario que mapea cada rol a sus skills con el peso asignado.
ROLES_SKILLS = {
    "Data Analyst": {
         "python": 0.5,
         "powerbi": 1.0,
         "r": 0.8,
         "excel": 0.7,
         "visualizacion de datos": 1.0, 
         "tableau": 0.9,
         "data analysis": 0.6,
         "estadistica descriptiva": 0.8,
         "analisis critico": 0.7, 
         "analisis": 0.6,
         "trabajoenequipo": 0.5,
         "comunicacion": 0.5,
         "data visualization": 1.0
    },
    "Data Engineer": {
         "python": 0.6,
         "etl": 1.0,
         "data lakes": 0.9,
         "apache spark": 1.0,
         "hadoop": 0.9,
         "apache kafka": 0.8,
         "sql": 1.0,
         "data warehouses": 0.9,
         "docker": 0.7,
         "gcp": 0.8,
         "aws": 0.8,
         "cloud computing": 0.8,
         "kubernetes": 0.8,
         "nosql": 0.7
    },
    "Data Scientist": {
         "python": 1.0,
         "r": 0.9,
         "machine learning": 1.0,
         "deep learning": 0.9,
         "tensorflow": 0.8,
         "pytorch": 0.8,
         "nlp": 0.8,
         "data mining": 0.7,
         "analisis predictivo": 0.9,
         "statistics": 0.7,
         "keras": 0.7
    },
    "Data Security & Privacy": {
         "seguridad": 1.0,
         "seguridad de sistemas": 0.9,
         "gdpr": 1.0,
         "iso 27001": 0.9,
         "gestion de riesgos": 0.8,
         "auditoria de datos": 0.7,
         "sistemas de seguridad": 0.9
    }
}

def identificar_rol(skills: list) -> str:
    """
    Dada una lista de skills, calcula el puntaje para cada rol según el diccionario
    y devuelve el rol con mayor puntaje. Si ningún rol acumula puntos, devuelve "Ninguna".
    """
    # Inicializar el puntaje para cada rol.
    puntuaciones = {rol: 0 for rol in ROLES_SKILLS}
    
    # Recorrer cada skill del input
    for skill in skills:
        skill_norm = normalizar(skill)
        for rol, mapping in ROLES_SKILLS.items():
            if skill_norm in mapping:
                puntuaciones[rol] += mapping[skill_norm]
    
    # Seleccionar el rol con el puntaje más alto
    rol_identificado = max(puntuaciones, key=puntuaciones.get)
    if puntuaciones[rol_identificado] == 0:
        return "Ninguna"
    return rol_identificado
