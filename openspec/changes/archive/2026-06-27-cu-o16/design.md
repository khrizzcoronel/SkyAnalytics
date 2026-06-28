## Context
Tenemos que garantizar que no se introducen "Breaking Changes" de forma inadvertida.

## Decisions
- Crearemos `backend/src/cicd/openapi_validator.py`.
- Recibirá un diccionario simulado que representa el YAML de la API.
- Buscará claves en `camelCase` (Regla RN-O16-002) y validará retrocompatibilidad simulando si un campo obligatorio fue eliminado.
