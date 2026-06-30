## Why
El dataset BTS 2024 contiene ~7.08M filas y ~1.25 GB. Cargarlo de una sola vez en PocketBase SQLite causaría timeouts y bloqueos. Se requiere un importador incremental con checkpoint JSON que permita reanudar la carga en lotes de 100k filas.

## What Changes
- Nuevo caso de uso `CU-O22` bajo el módulo `03-data-pipeline`.
- Contenedor Docker `importer` basado en `backend/import/import_flights.py`.
- Importación por chunks de 100,000 filas con checkpoint JSON persistente.
- IDs deterministas `fl<13digitos>` e inserciones `INSERT OR REPLACE` idempotentes.

## Capabilities
- `etl-ingestion-pipeline`: Importación incremental de dataset CSV a PocketBase SQLite.

## Acceptance Criteria
- El importador procesa 100k filas por ejecución.
- Reanuda desde el último checkpoint sin duplicados.
- Genera IDs deterministas y compatibles con `INSERT OR REPLACE`.
