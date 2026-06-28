## Why
La resolución rápida de Bugs impacta directamente la retención de clientes. Si un Enterprise tiene un error (500), el SLA manda a resolverlo en menos de 4 horas. Necesitamos un script de Triage automático.

## What Changes
- `support_triage.py`: Script que simula la recepción de un ticket, calcula la severidad en base al plan del cliente, y escala si es necesario.

## Capabilities
- `bug-triage-engine`: Asignación automática de severidad S1-S4.
