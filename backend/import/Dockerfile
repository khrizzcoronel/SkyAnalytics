FROM python:3.11-slim

WORKDIR /app

# SQLite3 y CSV se incluyen con la biblioteca estándar de Python, no se requieren dependencias externas de pip.
COPY import_flights.py .

# Ejecutar la importación de un chunk por defecto
CMD ["python", "import_flights.py"]
