---
module: 04-ml
primary_user: ML_ENGINEER
---
## ADDED Requirements

### Requirement: Checkpointing y Auto-Destrucción
El sistema MUST guardar el progreso en S3 y apagar el entorno al finalizar.

#### Scenario: Entrenamiento Exitoso
- **WHEN** entrena 50 epochs
- **THEN** guarda checkpoints y apaga la instancia al terminar.
