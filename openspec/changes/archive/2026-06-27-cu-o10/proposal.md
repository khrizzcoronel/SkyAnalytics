## Why
Si hemos consumido casi todo el tiempo de caída permitido en el mes (Error Budget), no debemos subir nuevos "features" que podrían introducir más bugs. Solo debemos permitir "Hotfixes" para estabilizar el sistema.

## What Changes
- `error_budget_gate.py`: Script para pipeline CI/CD que bloquea Pull Requests si el presupuesto de errores está casi agotado.

## Capabilities
- `error-budget-gatekeeper`: Regla que bloquea `feature` PRs si el budget consumido es > 80%.
