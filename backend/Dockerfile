FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Por defecto, el backend no tiene un servidor web expuesto aún (son scripts ETL/ML).
# Se puede sobreescribir este comando para ejecutar el monitor o scheduler.
CMD ["python", "src/tactical/data_quality_monitor.py"]
