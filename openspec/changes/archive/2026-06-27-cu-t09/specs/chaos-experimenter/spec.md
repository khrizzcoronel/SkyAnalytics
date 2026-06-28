## ADDED Requirements

### Requirement: Seguridad de Chaos Engineering
El sistema MUST abortar experimentos inyectados en entornos no permitidos.

#### Scenario: Protección de Producción
- **WHEN** se intenta inyectar partición de red en namespace `production`
- **THEN** el orquestador aborta (Kill Switch) inmediatamente sin aplicar cambios.
