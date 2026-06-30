---
module: 11-growth-monetization
primary_user: GROWTH_PM
---
## ADDED Requirements

### Requirement: Sincronización y Lead Scoring
El sistema MUST procesar leads y MUST asignar el multiplicador x2 a dominios logísticos.

#### Scenario: Atribución de campaña exitosa
- **WHEN** un lead entra con el término 'airlines'
- **THEN** su lead score se duplica y se sincroniza asíncronamente con HubSpot.
