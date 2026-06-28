## Context
Entrenar modelos Deep Learning masivos de forma segura.

## Decisions
- Crearemos `backend/src/ml/dl_experiment_runner.py`.
- **Regla RN-O20-001:** Simular entrenamiento por Epochs. Si el proceso avanza cada 10 epochs, hacer un "Checkpoint".
- **Regla RNF-O20-002:** Si finaliza, debe desaprovisionar automáticamente el nodo (simulado) para ahorrar costos.
