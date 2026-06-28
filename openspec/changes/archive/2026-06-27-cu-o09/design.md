## Context
Debemos validar el RTO de 15 minutos exigido por SOC 2.

## Decisions
- Crearemos `backend/src/dr/dr_drill_simulator.py`.
- Usaremos retardos simulados (`time.sleep`) para emular el tiempo que le toma a AWS RDS restaurar un Snapshot.
- Regla RN-O09-001: Si el tiempo de restauración supera 15 min, disparar alerta.
