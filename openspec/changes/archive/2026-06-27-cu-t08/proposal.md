## Why
Mantener los costos Cloud (FinOps) bajo control es esencial. Necesitamos un motor que evalúe si el gasto diario excede la proyección y genere recomendaciones automáticas de Rightsizing.

## What Changes
- `frontend/app/api/v1/tactico/finops/billing/route.ts`: Endpoint Next.js simulando la validación del Billing API.

## Capabilities
- `finops-analyzer`: Detección de picos de gasto (>20%) y recomendación de optimización (Rightsizing).
