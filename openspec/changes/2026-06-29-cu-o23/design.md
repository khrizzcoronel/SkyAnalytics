## Context
`vw_delay_analysis` contiene la serie temporal de retrasos. Comparar la distribución reciente contra un baseline histórico permite detectar degradación del modelo antes de que impacte predicciones.

## Decisions
- **Métrica PSI sobre `dep_delay`:** elegida por simplicidad e interpretabilidad.
- **Baseline 80% / Challenger 20%:** ordenados por `fl_date`, el 80% más antiguo es baseline, el 20% más reciente es challenger.
- **Umbrales:** <0.1 verde, 0.1-0.25 amarillo, >0.25 rojo.
- **Notificación Slack:** Webhook configurable vía `SLACK_WEBHOOK_URL`.

## Files Changed
- `backend/src/quality/dataset_drift_monitor.py`
- `specs/003-operativo/CU-O23.md` (a completar en Fase 2)

## Dependencies
- MonetDB con `vw_delay_analysis` poblada por `CU-O21`.
- Variable `SLACK_WEBHOOK_URL`.
