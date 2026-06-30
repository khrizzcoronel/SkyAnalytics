---
module: 09-seguridad
primary_user: SECOPS
---
## ADDED Requirements

### Requirement: Alerta y Auto-remediación WAF
El sistema MUST bloquear IPs infractoras y clasificar el incidente.

#### Scenario: Fuerza bruta
- **WHEN** un atacante realiza 500 intentos de inicio de sesión fallidos
- **THEN** la IP es bloqueada automáticamente (WAF) y se levanta alerta Sev2.
