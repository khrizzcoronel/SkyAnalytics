---
module: 02-api-vuelos
primary_user: CLIENT_API
---
## ADDED Requirements

### Requirement: Cuotas y HTTP 429
El sistema MUST validar un límite de `1000` peticiones por clave en un diccionario global. Si se supera, se MUST denegar el acceso.

#### Scenario: Soft Limit Reached
- **WHEN** el cliente hace su petición 1001 usando la misma `x-api-key`
- **THEN** el sistema retorna `HTTP 429 Too Many Requests`
- **AND** retorna el error "Monthly quota exceeded. Upgrade to Pro plan."
