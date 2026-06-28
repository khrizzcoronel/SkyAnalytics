## Why
Los entornos de desarrollo encendidos el fin de semana y los recursos huerfanos generan facturas de AWS altísimas (Waste). Necesitamos controles FinOps automatizados para apagar recursos fuera de horario y auditar gastos en los Pull Requests.

## What Changes
- `finops_optimizer.py`: Script que simula la evaluación de costos (Infracost) y el apagado (Snoozing) de recursos `Dev`.

## Capabilities
- `cloud-cost-optimizer`: Apagado automático de fin de semana y alertas de costo en PRs.
