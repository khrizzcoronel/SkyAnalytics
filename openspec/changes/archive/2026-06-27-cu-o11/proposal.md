## Why
Nuestros clientes B2B necesitan saber qué ha cambiado en la API cada semana. Escribir Release Notes a mano es lento y propenso a errores. Necesitamos generarlos automáticamente a partir del historial de commits.

## What Changes
- `changelog_generator.py`: Script que parsea los "Conventional Commits" de la semana, filtra los irrelevantes y genera un archivo Markdown (`changelog-vX.Y.Z.md`).

## Capabilities
- `auto-release-notes`: Generación de Markdown basado en `feat:` y `fix:`.
