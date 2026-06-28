## Why
Para cumplir nuestros SLAs, la infraestructura debe ser resiliente a fallos. Ejecutar pruebas de Chaos Network (Blackhole) ayuda a validar el auto-escalado (HPA).

## What Changes
- `frontend/app/api/v1/tactico/chaos/experiment/route.ts`: Endpoint Next.js simulando el disparador del experimento.

## Capabilities
- `chaos-experimenter`: Orquesta inyección de caos y mide la latencia P95 y auto-recuperación de pods.
