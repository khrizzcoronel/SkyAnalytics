## Why
Para maximizar los ingresos sin aumentar el churn, debemos poder experimentar con precios (A/B Testing) y evaluar la "Willingness to Pay" con significancia estadística.

## What Changes
- `frontend/app/api/v1/tactico/growth/abtest/route.ts`: Endpoint Next.js simulando un motor de A/B Testing para Pricing.

## Capabilities
- `growth-abtest`: Enrutamiento A/B, cálculo de significancia estadística (>95%) y protección de Grandfathering.
