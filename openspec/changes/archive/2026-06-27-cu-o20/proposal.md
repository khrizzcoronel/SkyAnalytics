## Why
Los experimentos de Deep Learning consumen mucha CPU/GPU y memoria. Ejecutarlos en la misma instancia de la API transaccional causará un Outage. Necesitamos un orquestador aislado que guarde checkpoints.

## What Changes
- `dl_experiment_runner.py`: Script que simula un orquestador de GPU aislando el entrenamiento y guardando checkpoints en S3.

## Capabilities
- `champion-challenger-evaluator`: Flujo de entrenamiento pesado con checkpointing y apagado automático (destrucción).
