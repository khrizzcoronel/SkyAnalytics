---
module: 08-devex
primary_user: DEVREL
---
## ADDED Requirements

### Requirement: Validación Linter y Diff
El sistema MUST rechazar contratos que no usen `snake_case` o que eliminen propiedades obligatorias.

#### Scenario: Breaking Change bloqueado
- **WHEN** se elimina la propiedad `delay_minutes` del contrato
- **THEN** la validación falla indicando "Breaking Change detectado".
