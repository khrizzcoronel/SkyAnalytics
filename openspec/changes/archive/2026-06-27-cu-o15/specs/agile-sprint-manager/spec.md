## ADDED Requirements

### Requirement: Sincronización Kanban Bidireccional
El sistema MUST transicionar automáticamente el estado de los tickets cuando ocurren eventos de Git.

#### Scenario: Branch a In Progress
- **WHEN** un desarrollador pushea una nueva branch `feature/SKY-101`
- **THEN** el tablero Kanban mueve SKY-101 de `To Do` a `In Progress`.
