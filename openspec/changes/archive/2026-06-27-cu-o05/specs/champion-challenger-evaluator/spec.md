## ADDED Requirements

### Requirement: Regla de Mejora Absoluta (> 2%)
El sistema SHALL comparar el MAPE actual (Champion) vs MAPE nuevo (Challenger).

#### Scenario: Nuevo Modelo Promovido
- **WHEN** Champion MAPE = 15.0% y Challenger MAPE = 12.0%
- **THEN** la mejora es del 3% (superior al 2%)
- **AND** el sistema marca el modelo como `Staging-Candidate`
- **AND** simula envío de Slack al Desarrollador.

#### Scenario: Nuevo Modelo Rechazado por Margen Pequeño
- **WHEN** Champion MAPE = 15.0% y Challenger MAPE = 14.5%
- **THEN** la mejora es solo del 0.5% (menor al 2%)
- **AND** el sistema aborta silenciosamente marcándolo como `Archived`.
