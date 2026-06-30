---
module: 06-observabilidad-sre
primary_user: SRE
---
## ADDED Requirements

### Requirement: Validación de RTO (Recovery Time Objective)
El orquestador de DR MUST calcular el tiempo total desde la petición de restauración hasta la disponibilidad de la DB. Si excede 15 min, MUST alertar.

#### Scenario: RTO excedido
- **WHEN** AWS RDS tarda 18 minutos simulados en restaurar
- **THEN** el orquestador falla el Drill y emite alerta de SLA Violado.
