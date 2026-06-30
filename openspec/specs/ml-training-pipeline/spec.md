---
module: 04-ml
primary_user: ML_ENGINEER
---
## ADDED Requirements

### Requirement: Determinismo
El script de entrenamiento SHALL utilizar semillas fijas (`RANDOM_SEED = 42`) para garantizar que la variabilidad de la precisión dependa exclusivamente de los datos frescos, no de la aleatoriedad de inicialización de la red.

#### Scenario: Evaluación MAPE
- **WHEN** el entrenamiento finaliza
- **THEN** el sistema calcula el Mean Absolute Percentage Error (MAPE) sobre el dataset de test.
