## Why
El dataset semilla de vuelos (BTS 2024) debe transformarse de un formato operativo/flat en `flights_raw` (PocketBase) a un modelo dimensional Star Schema en MonetDB que permita consultas analíticas rápidas para dashboards estratégicos y feature engineering de ML.

## What Changes
- Nuevo caso de uso `CU-O21` bajo el módulo `03-data-pipeline`.
- Script `backend/src/etl/etl_flights_to_monetdb.py` que:
  - Extrae incrementalmente desde `flights_raw` usando watermark `MAX(pb_created)`.
  - Genera dimensiones `dim_airline`, `dim_airport`, `dim_date` y tabla de hechos `fact_flights`.
  - Refresca vistas `vw_bsc_monthly` y `vw_delay_analysis`.
- Tabla `Quarantine_Data` en MonetDB para filas corruptas detectadas por `DataValidator`.

## Capabilities
- `etl-ingestion-pipeline`: Transformación PocketBase → MonetDB Star Schema con carga incremental idempotente.

## Acceptance Criteria
- El ETL corre a las 03:00 AM cron sin duplicar registros.
- Las vistas `vw_bsc_monthly` y `vw_delay_analysis` reflejan datos actualizados.
- Filas corruptas terminan en `Quarantine_Data` sin abortar el pipeline.
