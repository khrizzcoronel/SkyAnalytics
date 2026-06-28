## Context
Integración transparente entre el código y la herramienta de Project Management.

## Decisions
- Crearemos `backend/src/pm/agile_board_webhook.py`.
- Recibirá (simulado) payloads JSON de GitHub Webhooks.
- **Regla RN-O15-001:** Si el ticket viene de un Post-Mortem (Urgent/Bug), desplaza a los features y se pone en To-Do con máxima prioridad.
