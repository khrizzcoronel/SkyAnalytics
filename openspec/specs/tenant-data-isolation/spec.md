---
module: 01-identidad-acceso
primary_user: SRE
---
## ADDED Requirements

### Requirement: Filtro Estricto Multi-Tenant
Al refrescar y purgar, el sistema MUST operar sobre un `tenant_id` específico, evitando el sangrado de datos (Data Bleed) entre clientes competitivos.

#### Scenario: Privacidad Asegurada
- **WHEN** el proceso de purga de Delta Airlines (`tenant_123`) inicia
- **THEN** solo se refresca `mv_dashboard_123`
- **AND** la caché de American Airlines (`tenant_456`) permanece inalterada y segura.
