# Especificación de Caso de Uso: CU-O05

## 1. Nombre de la Funcionalidad
**Reentrenar Modelo de Retrasos**

## 2. Objetivo
Automatizar el reentrenamiento semanal de los modelos predictivos de Machine Learning (XGBoost/LightGBM) utilizando la información meteorológica y de vuelos más reciente (Feature Drift correction), y evaluar la necesidad técnica de reemplazar el modelo activo en producción.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Sistema (Pipeline CI/ML)
*   **Sistemas Externos / Actores Secundarios:** MLflow, Feast Feature Store / S3 Feature Store, GitHub Actions o GitHub Actions (Orquestador ML).

## 4. Contexto del Problema
El mercado aéreo es dinámico (ej. la temporada de invierno trae patrones distintos de retraso que la de verano). Un modelo de IA estático pierde precisión (Model Drift / Degradación). Es necesario que un pipeline extraiga las nuevas "features" de las últimas semanas, reentrene el algoritmo y compare si el nuevo modelo es mejor que el actual.

## 5. Requisitos Funcionales
*   **RF-O05-001:** El sistema debe activar el pipeline de reentrenamiento programado todos los fines de semana (domingos 04:00 UTC).
*   **RF-O05-002:** El sistema debe descargar el dataset de características técnicas pre-calculado desde AWS S3 (`s3://skyanalytics-ml/features/delay_prediction_2024.parquet`), el cual es generado desde MonetDB en el pipeline de feature engineering (CU-O24).
*   **RF-O05-003:** El sistema debe entrenar el modelo XGBoost utilizando la misma semilla (Random Seed) y pipeline que la versión productiva para asegurar reproducibilidad.
*   **RF-O05-004:** El sistema debe calcular el Mean Absolute Percentage Error (MAPE) del nuevo modelo usando un set de datos de prueba (Test Set) del mes más reciente.
*   **RF-O05-005:** El sistema debe comparar el MAPE del Modelo Nuevo ("Challenger") contra el MAPE del Modelo en Producción ("Champion").

## 6. Requisitos No Funcionales
*   **RNF-O05-001:** El proceso de reentrenamiento puede consumir horas y debe ejecutarse en instancias de cómputo efímeras (AWS EC2 Spot Instances) que se destruyan automáticamente al terminar para ahorrar costos (FinOps).
*   **RNF-O05-002:** Todo el output y logs de entrenamiento deben guardarse asíncronamente en S3 sin pérdida de datos en caso de que la instancia se apague sorpresivamente (Spot preemption).

## 7. Reglas de Negocio
*   **RN-O05-001 (Promoción Automática Champion-Challenger):** Si el Challenger mejora la precisión (MAPE) del Champion por un margen superior al 2% absoluto, el sistema etiqueta al nuevo modelo como `Staging-Candidate` en el registro. Nunca despliega directo a producción sin supervisión.
*   **RN-O05-002 (Criterio de Degradación):** Si el reentrenamiento genera un modelo peor que el histórico, el pipeline se cancela silenciosamente y se mantiene el modelo Champion operativo.

## 8. Entradas
*   Código de entrenamiento (Python scripts desde main branch).
*   Dataset de features en Parquet descargado de S3 (`s3://skyanalytics-ml/features/delay_prediction_2024.parquet`).

## 9. Salidas
*   **Artefacto:** Archivo modelo (.pkl / ONNX).
*   **Metadata:** Ejecución registrada en MLflow.
*   **Alerta:** Mensaje a Slack al Desarrollador (Tú) indicando si se halló un "Challenger" viable.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: El nuevo modelo derrota al Campeón
**Dado** que es domingo de madrugada y el pipeline de reentrenamiento se dispara
**Cuando** el entrenamiento finaliza y se comparan las métricas
**Entonces** el nuevo modelo obtiene un MAPE de 10% y el modelo viejo tiene un MAPE actual de 13%
**Y** el pipeline marca al nuevo modelo en MLflow como `Staging-Candidate`
**Y** envía un mensaje en Slack: "Nuevo Challenger listo para revisión: Mejora del 3% detectada. Por favor aprobar despliegue a Producción."

### Escenario 2: El nuevo modelo no presenta mejoras
**Dado** que el pipeline entrena sobre los datos de la última semana sin variaciones significativas de clima
**Cuando** evalúa el rendimiento sobre el set de prueba
**Entonces** el nuevo modelo tiene un MAPE de 13.5% vs el 13% del Champion
**Y** el sistema archiva (Archived) la corrida en MLflow
**Y** detiene el pipeline sin emitir alertas críticas, manteniendo el sistema productivo estable.

## 11. Criterios de Aceptación
*   **CA-O05-001:** El proceso de extracción del dataset (Feast Feature Store / S3) para el reentrenamiento debe generar datos que incluyan variables con un rezago máximo de 48 horas respecto a la fecha de ejecución (Frescura de Features).
*   **CA-O05-002:** Se genera un reporte de explicabilidad (SHAP Values) adjunto en MLflow para auditar por qué el nuevo modelo tomó ciertas decisiones en el test set.

## 12. Restricciones
*   Bajo ningún concepto un algoritmo promociona a Producción automáticamente, dado el impacto crítico que una predicción errónea tiene en el plan logístico de una aerolínea cliente.

## 13. Fuera de Alcance
*   Exposición de las inferencias por API. (Esto se delega al API Gateway que consume el modelo de Producción y se especifica en CU-O02).
