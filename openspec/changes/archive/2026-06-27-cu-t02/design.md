## Context
Exponer endpoints seguros para RapidAPI.

## Decisions
- Crearemos `frontend/app/api/v1/tactico/rapidapi/route.ts`.
- **Regla RNF-T02-001:** Validación rápida del header `X-RapidAPI-Proxy-Secret`.
- Si falta o es incorrecto, retornar `401 Unauthorized`.
- Si es válido, simular procesamiento exitoso.
