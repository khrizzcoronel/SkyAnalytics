## Context
PocketBase actúa como capa operativa/transaccional (OLTP). MonetDB es el data warehouse columnar (OLAP). El ETL es el puente entre ambos.

## Decisions
- **Incrementalidad por watermark:** se lee `MAX(pb_created)` de `fact_flights` y solo se procesan registros de `flights_raw` con `created > watermark`. Esto garantiza idempotencia.
- **Star Schema:** `fact_flights` con claves sustitutas hacia `dim_airline`, `dim_airport`, `dim_date`.
- **Quarantine en MonetDB:** las filas que fallan validaciones de negocio se insertan en `Quarantine_Data` (no CSV) para auditoría y re-procesamiento.
- **Vistas analíticas:** `vw_bsc_monthly` alimenta el BSC; `vw_delay_analysis` alimenta drift monitoring y feature engineering.
- **Conexión segura:** `MONETDB_PASS` solo por variable de entorno, sin defaults.

## Files Changed
- `backend/src/etl/etl_flights_to_monetdb.py`
- `backend/src/etl/data_validator.py`
- `specs/003-operativo/CU-O21.md` (a completar en Fase 2)

## Dependencies
- `flights_raw` poblada por `CU-O22`.
- MonetDB disponible y saludable.
