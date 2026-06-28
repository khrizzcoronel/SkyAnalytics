## Why
Si alguien cambia el contrato de la API y rompe la compatibilidad (Breaking Change) sin incrementar la versión, los clientes que la consumen fallarán. Necesitamos un linter estricto de OpenAPI en el CI/CD.

## What Changes
- `openapi_validator.py`: Script simulando validación Spectral y OpenAPI-Diff.

## Capabilities
- `openapi-linter`: Validación de convención (snake_case) y retrocompatibilidad.
