## Context
API Mock para Developer Portal.

## Decisions
- Crearemos `frontend/app/api/v1/tactico/devex/sandbox/route.ts`.
- **Regla RN-T07-002:** Rate limit simulado (10 req/min) usando un token generico temporal para evitar abusos desde el portal público.
- Si el token está ausente o vacío, rechazar. Si está presente, responder con datos meteorológicos sintéticos.
