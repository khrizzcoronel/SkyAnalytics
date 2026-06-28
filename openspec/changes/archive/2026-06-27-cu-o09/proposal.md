## Why
No basta con tomar Backups. Si un Ransomware borra los datos o un error humano suelta un `DROP TABLE`, necesitamos estar 100% seguros de que el Backup funciona y puede restaurarse en menos de 15 minutos (RTO). 

## What Changes
- `dr_drill_simulator.py`: Script que simulará el proceso automatizado de Restauración de Desastres (DR Drill).

## Capabilities
- `dr-drill-orchestrator`: Lógica para validar RTO y alertar si toma más de 15 minutos.
