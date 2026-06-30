---
module: 03-data-pipeline
primary_user: DATA_ENGINEER
---
## ADDED Requirements

### Requirement: Procesamiento en Chunks (Idempotencia)
El pipeline SHALL procesar los archivos CSV de gran tamaño leyendo en lotes (chunks) de `100_000` filas.
Antes de insertar el primer bloque, el pipeline MUST limpiar los datos cargados previamente para esa fecha y lote (DELETE idempotente).

#### Scenario: Reejecución segura
- **WHEN** el cronjob falla y se reinicia el mismo día
- **THEN** la base de datos de Staging elimina la carga fallida
- **AND** reingesta el nuevo CSV sin duplicar registros.
