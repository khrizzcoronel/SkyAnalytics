## Context
El dataset semilla debe poblar la tabla `flights_raw` de PocketBase de forma segura y reanudable.

## Decisions
- **Chunks de 100k filas:** evita timeouts de SQLite y mantiene uso de memoria bajo.
- **Checkpoint JSON:** `/data/importer_checkpoint.json` guarda `last_row` y `updated_at`.
- **IDs deterministas:** `fl` + índice con zero-padding de 13 dígitos. Esto permite `INSERT OR REPLACE` idempotente.
- **Contenedor one-shot:** `importer` se ejecuta con `restart: "no"` y debe invocarse repetidamente hasta completar el dataset.
- **Acceso directo a SQLite:** el importador escribe directamente en `/pb_data/data.db` compartido con el contenedor `pocketbase`. Esto es aceptable para carga semilla; el ETL posterior lee del mismo archivo.

## Files Changed
- `backend/import/import_flights.py`
- `backend/import/Dockerfile`
- `docker-compose.yml` (servicio `importer`)
- `specs/003-operativo/CU-O22.md` (a completar en Fase 2)

## Dependencies
- Archivo `flight_data_2024.csv` montado como volumen read-only.
- Tabla `flights_raw` existente en PocketBase (schema importado).
