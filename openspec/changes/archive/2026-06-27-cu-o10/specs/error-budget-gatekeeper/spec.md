## ADDED Requirements

### Requirement: Bloqueo de Despliegues por Error Budget
El CI/CD MUST bloquear cualquier despliegue a Producción si el Error Budget consumido es > 80%, a menos que el PR tenga la etiqueta `hotfix` o `reliability`.

#### Scenario: Feature bloqueado
- **WHEN** Budget Consumido es 85% y PR es `feature/nuevo-dashboard`
- **THEN** CI/CD falla y rechaza el merge.

#### Scenario: Hotfix permitido
- **WHEN** Budget Consumido es 90% y PR es `hotfix/fuga-memoria`
- **THEN** CI/CD permite el merge por excepción.
