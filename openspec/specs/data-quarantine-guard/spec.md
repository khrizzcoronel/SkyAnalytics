---
module: 03-data-pipeline
primary_user: DATA_ENGINEER
---
## ADDED Requirements

### Requirement: Filtrado Vectorial de Corrupción
El componente validador SHALL identificar los registros que no cumplan la estructura estricta (ej. `flight_id` == NULL).

#### Scenario: Fallo Parcial Seguro (Soft Failure)
- **WHEN** un archivo contiene 99,999 registros buenos y 1 defectuoso
- **THEN** la capa guarda el 1 defectuoso en formato JSON/CSV en `s3://sky-data-raw/quarantine/`
- **AND** continúa para insertar los 99,999 registros restantes sin causar `Aborted Transaction` en el lote masivo.
