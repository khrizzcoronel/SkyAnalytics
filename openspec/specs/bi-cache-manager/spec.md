---
module: 05-bi-estrategico
primary_user: C_LEVEL_EXEC
---
## ADDED Requirements

### Requirement: Refresco de Vistas y Purga de Caché
El sistema SHALL ejecutar un `REFRESH MATERIALIZED VIEW` simulado en la base de datos y posteriormente purgar la caché de BI para que refleje los nuevos datos.

#### Scenario: Carga Rápida UI
- **WHEN** el BI Cache Manager finaliza su trabajo
- **THEN** la nueva información pre-calculada de retrasos
- **AND** carga instantáneamente (<1.5s) para los clientes sin saturar el CPU.
