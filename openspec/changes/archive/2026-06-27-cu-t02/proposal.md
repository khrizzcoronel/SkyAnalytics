## Why
Monetizar las predicciones a través de RapidAPI requiere asegurar que solo las llamadas autorizadas por su proxy pasen. Además, necesitamos proteger nuestro cómputo interno con caché.

## What Changes
- `frontend/app/api/v1/tactico/rapidapi/route.ts`: API Route en Next.js para actuar como validador de proxy.

## Capabilities
- `rapidapi-gateway-auth`: Validación de tokens de RapidAPI y simulación de Rate Limit / Caché.
