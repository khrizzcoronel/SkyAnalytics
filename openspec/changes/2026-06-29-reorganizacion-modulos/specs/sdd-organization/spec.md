## ADDED Requirements

### Requirement: Domain-Driven Spec Organization
El proyecto SHALL organizar las especificaciones bajo `specs/<dominio-funcional>/` en lugar de `specs/<nivel-estratégico>/`.

#### Scenario: Nuevo desarrollador explora specs
- **WHEN** un desarrollador abre `specs/`
- **THEN** encuentra carpetas nombradas por dominio (ej. `03-data-pipeline`, `04-ml`)
- **AND** cada carpeta contiene CUs, plan, tasks, checklist y usuarios del dominio.

### Requirement: Canonical Role Matrix
El sistema SHALL mantener una matriz centralizada `matriz-usuarios-modulos.md` que defina qué roles acceden a qué módulos.

#### Scenario: Definición de RBAC
- **WHEN** se define una regla de acceso en PocketBase, middleware o API
- **THEN** la regla se basa en `matriz-usuarios-modulos.md`
- **AND** `CONSTITUTION.md` enumera los roles canónicos del sistema.
