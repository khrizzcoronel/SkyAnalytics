---
module: 03-data-pipeline
primary_user: DATA_ENGINEER
---
## ADDED Requirements

### Requirement: Detención del Pipeline (Circuit Breaker)
El sistema MUST calcular `bad_records / total_records`. Si esta tasa supera la tolerancia (ej. 1%), MUST abortar el flujo y retornar error.

#### Scenario: Schema Drift aborta la promoción a Core
- **WHEN** un lote tiene 5% de errores de esquema (ej. columnas faltantes)
- **THEN** el Circuit Breaker lanza una excepción `DataQualityThresholdError`
- **AND** la tabla `Fact_Flight` (Core) permanece intacta sin recibir los datos sucios.
