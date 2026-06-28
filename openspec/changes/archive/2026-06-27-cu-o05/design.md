## Context

SkyAnalytics ofrece predicciones de retraso a los usuarios finales. Estas predicciones provienen de un modelo entrenado históricamente (Champion). Con nuevos datos, necesitamos entrenar uno nuevo (Challenger) y promoverlo si, y sólo si, supera al modelo actual.

## Goals / Non-Goals

**Goals:**
- Simular el entrenamiento de un modelo para calcular un MAPE ficticio o usando un regresor simple de `scikit-learn`. (Para mantenerlo ligero, implementaremos una lógica Dummy que arroja un score con algo de variabilidad).
- Construir el "Evaluador" que compara los MAPEs.
- Mostrar por consola el registro estilo "MLflow" de si el modelo es rechazado (Degradado) o promovido a Candidate (Mejora > 2%).

**Non-Goals:**
- No instalaremos XGBoost ni entrenaremos redes neuronales profundas con terabytes en local. 
- No montaremos un servidor de MLflow; usaremos la salida estándar y archivos de texto plano para simular el Model Registry (Tracking Local).

## Decisions

- **Métrica Clave (MAPE):** Mean Absolute Percentage Error es excelente para explicar a negocio cuán equivocados estamos en porcentaje al predecir los minutos de retraso. (Ej: MAPE 10% significa que en promedio nos desviamos 10% del tiempo real).
- **Hard Rule de Promoción:** La regla RN-O05-001 estipula que la mejora debe ser "superior al 2% absoluto". (Es decir, si el Champion tiene 13% de error, el Challenger debe tener 10.99% o menos para ser promovido. Si saca 12%, se considera un margen demasiado pequeño para arriesgar Producción).
- **Despliegue Asistido:** Nunca desplegaremos directo. El estado máximo que alcanza un modelo exitoso es `Staging-Candidate`.

## Risks / Trade-offs

- **Reproducibilidad:** En ML real, si las semillas (seeds) cambian, los modelos varían.
  - *Mitigación:* Se establecerá en el script una constante simbólica `RANDOM_SEED = 42` para indicar que todo entrenamiento es determinista.
