## Context
El CI/CD necesita una validación automática (Status Check) para saber si permite o no un Merge.

## Decisions
- Crearemos `backend/src/cicd/error_budget_gate.py`.
- Se simulará la llamada a Sentry/Observability para consultar el % de Error Budget consumido.
- Si consumido > 80% y la etiqueta del PR NO es `hotfix` ni `reliability`, el script retorna exit code 1 (falla el pipeline).
