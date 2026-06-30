---
module: 01-identidad-acceso
primary_user: SRE
---
## ADDED Requirements

### Requirement: Revocación de permisos huérfanos
El sistema MUST revocar los permisos IAM de empleados que no se han utilizado en 90 días.

#### Scenario: Permiso antiguo
- **WHEN** el auditor IAM encuentra que `s3:DeleteBucket` lleva 100 días sin uso por el rol Dev
- **THEN** elimina la política automáticamente y documenta el hecho.
