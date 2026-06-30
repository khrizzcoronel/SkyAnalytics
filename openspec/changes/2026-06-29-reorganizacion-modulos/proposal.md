## Why
La organización original `specs/001-estrategico`, `specs/002-tactico`, `specs/003-operativo` agrupaba casos de uso por nivel de objetivo. Esto mezclaba funcionalidades disjuntas (p. ej. CU-O12 IAM y CU-O14 FAQ en "operativo") y dificultaba asignar equipos/usuarios dueños. La estructura por dominios funcionales mejora cohesión, ownership y escalabilidad.

## What Changes
- Reorganización física de `specs/` en 13 carpetas de dominio (`01-identidad-acceso` ... `13-okr-talento`).
- Migración de los 40 CUs a sus carpetas de dominio, preservando IDs originales.
- Creación de `plan.md`, `tasks.md`, `checklist.md` y `usuarios.md` por módulo.
- Actualización de `CONSTITUTION.md` con taxonomía de módulos y roles canónicos.
- Creación de `specs/000-sistema-general/matriz-usuarios-modulos.md`.
- Archivo histórico de plan/tasks/checklist originales en `historial-specs-por-objetivo/`.

## Capabilities
- `sdd-organization`: Estructura de especificación y gobernanza del proyecto.

## Acceptance Criteria
- Los 40 CUs residen en carpetas de dominio.
- Cada módulo tiene plan/tasks/checklist/usuarios.
- CONSTITUTION.md refleja la nueva organización y roles canónicos.
