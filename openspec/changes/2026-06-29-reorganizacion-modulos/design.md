## Context
El repositorio creció desde 3 niveles (estratégico/táctico/operativo) hasta 40 CUs. La taxonomía por objetivo ya no escalaba ni reflejaba la arquitectura real.

## Decisions
- **Dominios funcionales:** agrupar CUs por área de negocio/tecnología (Identidad, Data Pipeline, ML, BI, SRE, etc.).
- **Usuario dueño por módulo:** cada dominio tiene un rol principal responsable (Data Engineer, ML Engineer, SRE, etc.).
- **Preservar IDs de CU:** no renombrar CUs para mantener trazabilidad con OpenSpec archive histórico.
- **Módulos con plan/tasks/checklist propios:** cada dominio gestiona su propio backlog y QA.
- **Matriz de permisos centralizada:** `matriz-usuarios-modulos.md` define RBAC canónico.

## Files Changed
- `specs/000-sistema-general/CONSTITUTION.md`
- `specs/000-sistema-general/matriz-usuarios-modulos.md`
- `specs/000-sistema-general/historial-specs-por-objetivo/`
- `specs/01-identidad-acceso/` ... `specs/13-okr-talento/`
- `openspec/specs/*/spec.md` (frontmatter `module` / `primary_user`)
