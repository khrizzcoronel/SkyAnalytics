## ADDED Requirements

### Requirement: Triage Automatizado
El sistema MUST asignar S1 y disparar alerta si el cliente es Enterprise y reporta una caída total.

#### Scenario: Alerta S1
- **WHEN** un cliente "Enterprise" envía un ticket con palabra clave "Crash"
- **THEN** se clasifica como S1 (Critical) y se escala.
