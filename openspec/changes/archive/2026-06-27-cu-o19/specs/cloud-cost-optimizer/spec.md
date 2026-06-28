## ADDED Requirements

### Requirement: Snoozing Automático y Control de Gasto
El sistema MUST apagar instancias de desarrollo en fin de semana y MUST bloquear PRs costosos.

#### Scenario: Snoozing Aplicado
- **WHEN** es viernes por la noche
- **THEN** la instancia `db.t3.medium` con tag `Dev` se apaga automáticamente.
