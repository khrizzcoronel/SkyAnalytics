## Why
Los modelos ML de predicción de retrasos se degradan cuando la distribución de los datos de entrada cambia (data drift). Es necesario monitorear semanalmente el drift del dataset de vuelos usando PSI sobre `vw_delay_analysis` y alertar a #data-ops cuando PSI > 0.25.

## What Changes
- Nuevo caso de uso `CU-O23` bajo el módulo `03-data-pipeline`.
- Script `backend/src/quality/dataset_drift_monitor.py` que calcula PSI sobre `dep_delay`.
- Alerta Slack a `#data-ops` cuando PSI > 0.25.

## Capabilities
- `data-quality-suite`: Monitoreo de data drift vía Population Stability Index (PSI).

## Acceptance Criteria
- El monitor corre los lunes a las 06:00 AM.
- Calcula PSI entre baseline (80% histórico) y challenger (20% reciente).
- Emite alerta Slack cuando PSI > 0.25 (rojo), aviso amarillo 0.1-0.25, verde < 0.1.
