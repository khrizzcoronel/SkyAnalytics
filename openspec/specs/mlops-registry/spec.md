---
module: 04-ml
primary_user: ML_ENGINEER
---
## ADDED Requirements

### Requirement: Validación de Modelo en Producción
El sistema MUST bloquear promociones a `Production` si el modelo no alcanza el criterio de exactitud.

#### Scenario: MAPE Alto
- **WHEN** el MAPE del modelo es 18.2% y se pide pasar a `Production`
- **THEN** el sistema arroja un error y mantiene el estado en `Staging`.
