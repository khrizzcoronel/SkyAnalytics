## Why
Necesitamos organizar el trabajo en Sprints (Ciclos) para tener predictibilidad. Un gestor ágil (GitHub Issues) integrado bidireccionalmente nos ayuda a saber qué está haciendo el desarrollador sin micromanagement.

## What Changes
- `agile_board_webhook.py`: Simulación de un webhook handler que procesa eventos de GitHub y mueve tarjetas (Issues) automáticamente en el tablero Kanban.

## Capabilities
- `agile-sprint-manager`: Mueve tickets automáticamente basados en acciones de Git (Branch -> In Progress, PR -> In Review, Merge -> Done).
