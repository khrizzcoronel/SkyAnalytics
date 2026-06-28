## Context
El CI/CD generará el Changelog todos los viernes.

## Decisions
- Crearemos `backend/src/cicd/changelog_generator.py`.
- Recibirá una lista de commits simulada.
- Filtrará `chore:` y `ci:` (Regla RN-O11-002).
- Si hay un `BREAKING CHANGE`, marcará la release como versión MAJOR (Regla RN-O11-001).
