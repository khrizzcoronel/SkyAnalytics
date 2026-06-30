---
module: 03-data-pipeline
primary_user: DATA_ENGINEER
---
## ADDED Requirements

### Requirement: Pydantic Data Contract
El sistema SHALL validar que cada fila extraída de Staging cumpla un modelo estricto (ej. el estatus solo puede ser ON_TIME, DELAYED o CANCELLED, y el monto debe ser positivo).

#### Scenario: Fila inválida detectada por contrato
- **WHEN** la validación lee una fila donde `status = 'UNKNOWN'`
- **THEN** Pydantic arroja `ValidationError`
- **AND** la fila se cuenta como "Bad Record" en las estadísticas.
