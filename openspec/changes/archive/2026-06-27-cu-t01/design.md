## Context
Growth Hacking mediante integración con HubSpot (API Route en Next.js).

## Decisions
- Crearemos `frontend/app/api/v1/tactico/hubspot/route.ts`.
- **Regla RN-T01-001:** Un multiplicador x2 en el Lead Score si el email incluye términos aeronáuticos/logísticos.
- **Regla RN-T01-002:** Calcular CAC por campaña basado en el gasto y los tenants activados.
