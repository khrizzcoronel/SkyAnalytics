## Context
Data Quality y Circuit Breaker en Python.

## Decisions
- Crearemos `backend/src/tactical/data_quality_monitor.py`.
- **Regla RN-T04-002 (Circuit Breaker):** Ningún dato sin `flight_id` válido pasará la validación.
- Simular el alertamiento a `#data-ops` en Slack.
