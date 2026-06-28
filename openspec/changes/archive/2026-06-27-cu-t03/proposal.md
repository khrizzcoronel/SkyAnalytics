## Why
Evitar el ClickOps en AWS para garantizar que la infraestructura sea inmutable y pase las pruebas de seguridad (tfsec) antes del despliegue.

## What Changes
- `frontend/app/api/v1/tactico/cicd/guard/route.ts`: Endpoint simulado en Next.js para auditar PRs de infraestructura.

## Capabilities
- `iac-pipeline-guard`: Análisis estático simulado que bloquea recursos como Buckets S3 públicos.
