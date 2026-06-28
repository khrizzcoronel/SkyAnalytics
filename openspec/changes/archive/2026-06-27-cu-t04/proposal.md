## Why
Monitorear la calidad de datos y los pipelines ETL es crítico para evitar que datos corruptos o con "schema drift" lleguen a los dashboards o modelos ML.

## What Changes
- `backend/src/tactical/data_quality_monitor.py`: Script en Python simulando validación de dbt y Circuit Breaker.

## Capabilities
- `data-quality-monitor`: Observabilidad ETL y bloqueo de datos malformados.
