## Context
A/B Testing para Pricing.

## Decisions
- Crearemos `frontend/app/api/v1/tactico/growth/abtest/route.ts`.
- **Regla RN-T10-001:** Retornar sugerencia de despliegue si la significancia estadística (P-Value simulado) supera el 95%.
- **Regla RN-T10-002:** Si el cliente ya existe (Grandfathering), forzar la variante heredada.
