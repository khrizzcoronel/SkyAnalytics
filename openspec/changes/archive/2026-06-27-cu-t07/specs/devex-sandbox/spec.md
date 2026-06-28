## ADDED Requirements

### Requirement: Sandbox Interactivo para SDKs
El sistema MUST retornar un JSON mockeado de forma rápida a los usuarios del portal sin consumir tokens productivos.

#### Scenario: Mock Request
- **WHEN** el usuario prueba el endpoint de clima en Sandbox
- **THEN** retorna datos climáticos sintéticos bajo 1 segundo.
