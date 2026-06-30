---
module: 06-observabilidad-sre
primary_user: SRE
---
## ADDED Requirements

### Requirement: Cultura Blameless en Post-Mortems
El sistema MUST generar la plantilla de RCA y MUST verificar (simulado) que no se usen nombres propios para culpar a individuos.

#### Scenario: Generación exitosa
- **WHEN** un incidente Sev1 se resuelve
- **THEN** se crea el archivo `post_mortem_YYYY-MM-DD.md` con las secciones obligatorias.
