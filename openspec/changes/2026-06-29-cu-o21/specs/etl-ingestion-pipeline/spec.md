## ADDED Requirements

### Requirement: Star Schema ETL from PocketBase to MonetDB
El pipeline SHALL transformar los registros de `flights_raw` (PocketBase) en un Star Schema dimensional en MonetDB compuesto por `dim_airline`, `dim_airport`, `dim_date` y `fact_flights`.

#### Scenario: Carga incremental diaria
- **WHEN** el cronjob diario ejecuta `etl_flights_to_monetdb.py`
- **THEN** el sistema lee solo los registros de `flights_raw` con `created > MAX(pb_created)` de `fact_flights`
- **AND** genera/actualiza las dimensiones necesarias
- **AND** inserta los nuevos hechos en `fact_flights`
- **AND** refresca las vistas `vw_bsc_monthly` y `vw_delay_analysis`.

### Requirement: Quarantine en MonetDB
El pipeline SHALL desviar filas corruptas (según `DataValidator`) a una tabla `Quarantine_Data` en MonetDB con columna `quarantine_reason`.

#### Scenario: Fila corrupta no aborta el pipeline
- **WHEN** el ETL encuentra 5 filas con `distance <= 0`
- **THEN** esas filas se insertan en `Quarantine_Data`
- **AND** las filas válidas continúan hacia `fact_flights`
- **AND** el proceso termina con éxito.
