## Context
Los tickets de soporte entran crudos. Hay que clasificarlos para cumplir SLAs.

## Decisions
- Usar un script Python simple (`backend/src/support/support_triage.py`).
- Regla: Enterprise + "500 Error" o "Blocker" = Severidad S1.
- Regla: Si es S1, emite alerta de Slack (simulada) para acción inmediata.
