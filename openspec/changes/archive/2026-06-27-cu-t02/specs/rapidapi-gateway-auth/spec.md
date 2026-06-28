## ADDED Requirements

### Requirement: Validación RapidAPI
El sistema MUST bloquear peticiones que no provengan del proxy de RapidAPI.

#### Scenario: Bypass bloqueado
- **WHEN** un cliente hace un GET sin el secreto correcto
- **THEN** recibe HTTP 401 Unauthorized y no se gasta cómputo.
