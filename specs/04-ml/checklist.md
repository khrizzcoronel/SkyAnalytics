# Checklist de Validación: Machine Learning

## CU-O05 — Reentrenar Modelo de Retrasos
- [ ] **CA-O05-001:** El proceso de extracción del dataset (Feast Feature Store / S3) para el reentrenamiento debe generar datos que incluyan variables con un rezago máximo de 48 horas respecto a la fecha de ejecución (Frescura de Features).
- [ ] **CA-O05-002:** Se genera un reporte de explicabilidad (SHAP Values) adjunto en MLflow para auditar por qué el nuevo modelo tomó ciertas decisiones en el test set.

## CU-O20 — Ejecutar Experimentos de Deep Learning
- [ ] **CA-O20-001:** La interrupción de una instancia Spot a la mitad de un experimento no corrompe el entrenamiento; un nuevo nodo debe ser capaz de levantar el último Checkpoint y reanudar el entrenamiento matemático sin intervención humana.

## CU-T05 — Entrenar y Versionar Modelos ML
- [ ] **CA-T05-001:** Cualquier modelo entrenado puede ser reproducido de manera idéntica ejecutando el mismo commit de código con el mismo Dataset ID proveniente de Feast Feature Store / S3.
- [ ] **CA-T05-002:** El reporte SHAP es obligatorio; el entrenamiento falla a nivel de pipeline si no se logra generar la explicabilidad del modelo.
