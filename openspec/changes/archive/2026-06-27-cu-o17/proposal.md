## Why
Si un servicio origen cambia el nombre o tipo de una columna, los pipelines de ML y Dashboards fallan (Schema Drift). Validar Data Contracts previene esto.

## What Changes
- `data_contract_validator.py`: Script de validación de contrato de datos que compara esquemas entrantes con esquemas pactados.

## Capabilities
- `schema-registry-validator`: Valida Backward/Forward compatibility y aísla datos corruptos en una Dead Letter Queue (DLQ).
