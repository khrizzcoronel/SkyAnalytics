## Why

Los modelos de Machine Learning sufren de "Model Drift" a medida que los patrones del mundo real cambian (ej. cambios climáticos por estaciones o nuevas rutas de aerolíneas). Un modelo predictivo estancado empieza a dar predicciones de retraso incorrectas. Necesitamos un pipeline automatizado que reentrene el modelo y lo evalúe objetivamente contra la versión actual (Champion vs Challenger) para asegurar que la precisión de SkyAnalytics mejore continuamente.

## What Changes

- **Pipeline de Entrenamiento ML**: Creación de un script en Python que simule el entrenamiento de un modelo de Machine Learning (Dummy/Mocked para este caso, o Scikit-Learn/XGBoost si instalamos dependencias) para predecir los retrasos (`delay_minutes`).
- **Lógica Champion-Challenger**: Comparación de la métrica MAPE (Mean Absolute Percentage Error) del nuevo modelo contra el viejo.
- **Registro (Tracking)**: Simulación de almacenamiento en un "Feature Store/Model Registry" local que dicte si el modelo debe ser promovido a candidato.

## Capabilities

### New Capabilities
- `ml-training-pipeline`: Componente que reentrena algoritmos y calcula métricas (MAPE).
- `champion-challenger-evaluator`: Guardián de precisión que decide si el modelo se descarta o pasa a revisión manual.

### Modified Capabilities
- 

## Impact

- **Backend (Python)**: Nueva carpeta `backend/src/ml/` para la lógica de Inteligencia Artificial.
- **Inteligencia**: El sistema se vuelve adaptativo sin requerir la intervención humana directa, salvo para la aprobación final del despliegue.
