## Context
El sistema de soporte se integra con la base de conocimientos (simulada) para crear plantillas de Post-Mortem.

## Decisions
- Crearemos `backend/src/support/post_mortem_generator.py`.
- Generará un Markdown con secciones `Timeline`, `Root Cause (5 Whys)` y `Action Items`.
- **Regla RN-O13-001:** Se rechazarán los textos si contienen nombres (ej. "Juan", "Pedro") simulando un check "Blameless".
