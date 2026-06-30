---
module: 05-bi-estrategico
primary_user: C_LEVEL_EXEC
---
## ADDED Requirements

### Requirement: Consumo de Error Budget
El sistema SHALL mostrar un medidor que calcule el porcentaje consumido del Error Budget (4.38 min/mes) en función del Uptime real consultado a MonetDB (`vw_uptime_telemetry`).

#### Scenario: Alerta de Error Budget
- **WHEN** el presupuesto de error consumido es del 85%
- **THEN** el panel se tiñe de color rojo y sugiere (visualmente) la interrupción de despliegues.

### Requirement: Refresco Asíncrono
El sistema MUST actualizar los datos de la vista de ingeniería automáticamente sin recargar la pantalla completa.

#### Scenario: Actualización de SLA
- **WHEN** el usuario permanece en la pestaña `/dashboard/engineering` por más de 30 segundos
- **THEN** el sistema efectúa una petición XHR a `/api/v1/estrategico/engineering/health` y refresca el Uptime.
