## ADDED Requirements

### Requirement: Bloqueo de Infraestructura Insegura
El sistema MUST analizar estáticamente el código y bloquear configuraciones inseguras.

#### Scenario: Fallo tfsec
- **WHEN** un manifiesto expone el bucket a internet
- **THEN** el sistema rechaza el PR y no ejecuta apply.
