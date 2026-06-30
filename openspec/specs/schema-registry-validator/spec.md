---
module: 03-data-pipeline
primary_user: DATA_ENGINEER
---
## ADDED Requirements

### Requirement: Validación de Contratos
El sistema MUST validar los datos entrantes contra el contrato estático.

#### Scenario: Schema Drift Bloqueado
- **WHEN** el origen elimina `flight_number`
- **THEN** la validación falla indicando "Schema Violation" y se envía a DLQ.
