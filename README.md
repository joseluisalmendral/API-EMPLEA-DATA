# 📊 API para Emplea Data

Esta API está desarrollada con **FastAPI** y se conecta a una base de datos **MongoDB Atlas**. Proporciona datos en formato JSON relacionados con la base de datos de **Emplea Data**, listos para ser utilizados en aplicaciones front-end.

[DOCS API DESPLEGADA](https://api-emplea-data.onrender.com/docs)

(puede tardar un poco debido a que está con el free plan y se apaga por inactividad pero al recibir llamadas se levanta al minuto)

---

## 🚀 **Características**
- Conexión segura con MongoDB Atlas mediante variables de entorno.
- Endpoints para obtener información de la base de datos de **Emplea Data**.
- Respuesta en formato JSON, fácil de consumir en aplicaciones front-end.
- Desplegable en **Render** o cualquier plataforma compatible con FastAPI.

---

## 📂 **Estructura del Proyecto**
```
/mi_api_render
│── .env                   # Variables de entorno (NO se sube al repositorio)
│── .gitignore             # Archivos ignorados por Git
│── config.py              # Configuración de la API (carga de variables)
│── Dockerfile             # Configuración opcional para despliegue con Docker
│── main.py                # Código principal de la API
│── README.md              # Documentación del proyecto
│── requirements.txt       # Dependencias de Python
│── start.sh               # Script para ejecutar el servidor
```

---

## 🛠️ **Requisitos**
- **Python 3.9+**
- Cuenta en **MongoDB Atlas** con una base de datos configurada.
- Dependencias instaladas desde `requirements.txt`.

---

## ⚙️ **Configuración del Proyecto**
1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/mi-api-render.git
   cd mi-api-render
   ```

2. **Crea un archivo `.env`**:
   Este archivo debe contener las siguientes variables:
   ```
   DB_PASS=tu_password
   DB_NAME=nombre_base_datos
   DB_COLLECTION=nombre_coleccion
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta el servidor**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

5. **Accede a la API**:
   - Visita: `http://127.0.0.1:8000`
   - Documentación interactiva: `http://127.0.0.1:8000/docs`

---

## 🛠️ **Variables de Entorno en Render**
1. Ve al panel de control de Render.
2. Agrega las siguientes variables en **Environment Variables**:
   - `DB_PASS`: Tu contraseña de MongoDB Atlas.
   - `DB_NAME`: El nombre de tu base de datos.
   - `DB_COLLECTION`: El nombre de la colección a consultar.

---

## 📊 **Endpoints**
### `/`
- **Descripción**: Endpoint de prueba para verificar que la API funciona.
- **Método**: `GET`
- **Respuesta**:
  ```json
  {
    "message": "API funcionando correctamente"
  }
  ```

### `/prueba`
- **Descripción**: Devuelve información procesada de la base de datos.
- **Método**: `GET`
- **Respuesta**:
  ```json
  {
    "data": [
      {"key1": "valor1", "key2": "valor2"},
      ...
    ]
  }
  ```

---

## 🐳 **Opcional: Despliegue con Docker**
Si prefieres usar Docker, crea una imagen con el siguiente comando:
```bash
docker build -t mi-api-render .
```

Ejecuta el contenedor:
```bash
docker run -p 8000:8000 mi-api-render
```

---

## 🚀 **Despliegue en Render**
1. Sube tu código a un repositorio en GitHub.
2. Crea un nuevo **Web Service** en Render.
3. Configura las **Environment Variables** en Render con los valores del archivo `.env`.
4. Define el comando de inicio:
   ```bash
   bash start.sh
   ```

---

## 👨‍💻 **Contribuciones**
Las contribuciones son bienvenidas. Si tienes ideas para mejorar esta API, abre un **issue** o envía un **pull request**.

---

## 📄 **Licencia**
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
