## ADDED Requirements

### Requirement: Filtrado de Commits y Semantic Versioning
El generador MUST ignorar commits internos y MUST incrementar la versión correctamente si se detectan breaking changes.

#### Scenario: Changelog Menor
- **WHEN** hay 2 features y 1 fix
- **THEN** se documentan bajo la misma versión Minor.

#### Scenario: Ruido ignorado
- **WHEN** solo hay commits `chore:` o `ci:`
- **THEN** no se genera changelog.
