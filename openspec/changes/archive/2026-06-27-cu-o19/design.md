## Context
Integrar controles financieros operativos en el flujo de ingeniería.

## Decisions
- Crearemos `backend/src/ops/finops_optimizer.py`.
- **Regla RN-O19-001:** Apagar recursos con la etiqueta `Environment=Dev` si no tienen `FinOps-Snooze=False`.
- **Regla RN-O19-002:** Si el incremento de costo de un PR excede el presupuesto (ej. +$1000), requerir revisión obligatoria.
