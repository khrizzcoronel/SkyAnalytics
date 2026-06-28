## Context
MLOps Tracking y validación de MAPE.

## Decisions
- Crearemos `backend/src/tactical/mlops_registry.py`.
- **Regla RN-T05-001:** Un modelo no puede transicionar a Producción si su MAPE > 15%.
- Simular la generación de SHAP values (explicabilidad).
