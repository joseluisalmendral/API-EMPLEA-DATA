# Usa una imagen base ligera para Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el contenedor
EXPOSE 8000

# Comando de inicio
CMD ["sh", "start.sh"]
