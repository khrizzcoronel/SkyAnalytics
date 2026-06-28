## ADDED Requirements

### Requirement: Análisis eNPS con Privacidad
El sistema MUST calcular el eNPS de los equipos pero MUST ocultar datos si hay riesgo de identificación.

#### Scenario: Alerta de Burnout
- **WHEN** el eNPS de un equipo es 5
- **THEN** el sistema alerta sobre riesgo de fuga y sugiere retención 1:1.
