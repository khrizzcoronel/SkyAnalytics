---
module: 11-growth-monetization
primary_user: GROWTH_PM
---
## ADDED Requirements

### Requirement: Enrutamiento A/B y Grandfathering
El sistema MUST proteger el precio de clientes existentes mientras experimenta con nuevos prospectos.

#### Scenario: Grandfathering Activo
- **WHEN** un cliente antiguo con suscripción activa visita la página de precios
- **THEN** se le asigna siempre la "Variante A (Legacy)" independientemente del experimento.
