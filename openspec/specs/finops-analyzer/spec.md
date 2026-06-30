---
module: 10-finops
primary_user: FINOPS_MANAGER
---
## ADDED Requirements

### Requirement: Alerta Temprana de Costos (FinOps)
El sistema MUST analizar la variación del gasto diario frente al presupuestado.

#### Scenario: Pico de Gasto en S3
- **WHEN** el costo del día es \$150 y el forecast era \$100 (desviación del 50%)
- **THEN** el sistema envía una alerta roja a Slack y marca el servicio como en sobrecosto.
