## Context
Seguridad en la integración continua de Infraestructura como Código.

## Decisions
- Crearemos `frontend/app/api/v1/tactico/cicd/guard/route.ts`.
- **Regla RN-T03-002:** Si un manifiesto contiene `acl = "public-read"` en un S3, el pipeline debe fallar.
- El script simulará leer un payload de webhook de GitHub Actions (PR abierto) y responder con Success o Blocked.
