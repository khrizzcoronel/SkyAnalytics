## 1. Módulo ML Training

## 1. Módulo ML Training

- [x] 1.1 Crear la carpeta `backend/src/ml/`.
- [x] 1.2 Desarrollar el script `train_model_stub.py` que contenga una función `train_and_evaluate()` que simule el proceso y devuelva un puntaje (MAPE). Se pasará una semilla para determinismo.

## 2. Champion-Challenger Evaluator

- [x] 2.1 En el mismo u otro archivo orquestador, implementar la clase `ModelRegistryEvaluator`.
- [x] 2.2 Escribir el método `evaluate(champion_mape, challenger_mape)` que implemente la regla RN-O05-001 (Mejora > 2.0).
- [x] 2.3 Si pasa, imprimir mensaje simulando envío a Slack y etiquetar como `Staging-Candidate`. Si no, etiquetar como `Archived`.

## 3. Pruebas y Ensamblaje

- [x] 3.1 Crear un bloque `__main__` que ejecute dos corridas: una donde el modelo mejora 3% y otra donde empeora/mejora poco. Observar los resultados.
