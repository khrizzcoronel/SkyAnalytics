## ADDED Requirements

### Requirement: Validación de Controles SOC2 y GDPR
El sistema MUST escanear los recursos e identificar aquellos no cifrados o en regiones incorrectas.

#### Scenario: Fallo GDPR
- **WHEN** un bucket con datos europeos está en `us-east-1`
- **THEN** se marca en ROJO el control de Residencia de Datos.
