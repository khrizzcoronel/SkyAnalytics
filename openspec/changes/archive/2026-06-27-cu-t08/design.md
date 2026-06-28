## Context
Monitoreo FinOps y Optimización Cloud.

## Decisions
- Crearemos `frontend/app/api/v1/tactico/finops/billing/route.ts`.
- **Regla RN-T08-001:** Alertar a `#finops` en Slack si el costo diario vs la proyección mensual tiene un delta > 20%.
- Generar una recomendación simulada de rightsizing (ej. `m5.2xlarge` -> `m5.xlarge`).
