## 1. Setup y Simulación (Python)

## 1. Setup y Simulación (Python)

- [x] 1.1 Instalar Pandas (`pip install pandas`).
- [x] 1.2 Crear un script generador de datos Mock (`backend/src/etl/generate_mock_csv.py`) para generar un archivo `daily_flights.csv` de 5,000 líneas (incluyendo algunas defectuosas).

## 2. Ingesta y Cuarentena

- [x] 2.1 Crear `backend/src/etl/data_validator.py` con una función `separate_bad_rows()` que evalúe nulos usando máscaras de Pandas.
- [x] 2.2 Crear el script orquestador `backend/src/etl/ingestion_job.py` que lea el CSV en chunks.
- [x] 2.3 Implementar la escritura de filas corruptas al disco local simulando `s3://sky-data-raw/quarantine/`.

## 3. Carga en Staging

- [x] 3.1 Construir un `StagingDatabaseStub` (simulador) que acepte la inserción masiva (`insert_many`) de las filas limpias.
- [x] 3.2 Verificar ejecutando el script y comprobando que las filas defectuosas se separaron y las limpias llegaron al Stub.
