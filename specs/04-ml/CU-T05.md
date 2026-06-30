# Especificación de Caso de Uso: CU-T05

## 1. Nombre de la Funcionalidad
**Entrenar y Versionar Modelos ML**

## 2. Objetivo
Permitir a los desarrolladores diseñar, ejecutar experimentos, entrenar y versionar modelos de Machine Learning (ej. predicción de retrasos, clima) en un entorno estructurado (MLOps) garantizando trazabilidad total de hiperparámetros y métricas.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** MLflow (Tracking y Model Registry), Archivos Parquet locales, Entorno local o Google Colab o clúster de cómputo PaaS.

## 4. Contexto del Problema
Desarrollar modelos de ML en notebooks locales de forma aislada genera la incapacidad de reproducir experimentos, pérdida de modelos antiguos y dificultad para comparar qué combinación de hiperparámetros produjo el mejor MAPE (Mean Absolute Percentage Error). Se requiere adoptar una filosofía MLOps rigurosa.

## 5. Requisitos Funcionales
*   **RF-T05-001:** El sistema (vía SDK interno) debe registrar automáticamente en **MLflow** cada corrida (Run) de experimentación, guardando: código, hiperparámetros, métricas (MAPE, RMSE) y artefactos (el modelo serializado en formato `.pkl` u ONNX).
*   **RF-T05-002:** El sistema debe consumir las características (Features) unificadas y pre-calculadas directamente desde **Feast Feature Store / S3** para garantizar que los datos usados en entrenamiento sean idénticos a los usados en inferencia (evitando *train-serving skew*).
*   **RF-T05-003:** El sistema debe proveer una interfaz visual (MLflow UI) para comparar métricas entre diferentes ejecuciones y modelos en paralelo.
*   **RF-T05-004:** El Desarrollador (Tú) debe poder transicionar un modelo entre estados de registro: `Staging`, `Production`, y `Archived` mediante aprobación formal.

## 6. Requisitos No Funcionales
*   **RNF-T05-001 (Trazabilidad):** Toda ejecución debe estar enlazada al Hash del Commit de Git exacto que la produjo.
*   **RNF-T05-002 (Explainability):** El proceso de entrenamiento debe generar un reporte de Feature Importance basado en **SHAP values** y almacenarlo como un artefacto adjunto al modelo para auditoría de cajas negras.

## 7. Reglas de Negocio
*   **RN-T05-001 (Criterio de Promoción):** Para que un modelo pase de `Staging` a `Production`, su MAPE debe ser estrictamente menor o igual al 15% (MAPE $\leq$ 15%) y debe superar estadísticamente al modelo actual en producción.
*   **RN-T05-002 (A/B Testing en Inferencia):** Una vez promocionado a producción, el nuevo modelo comienza inicialmente con un enrutamiento de tráfico del 10% (Canary Release) antes de asimilar el 100% de la carga de inferencia.

## 8. Entradas
*   Variables de Configuración: Hiperparámetros de los algoritmos (XGBoost / LightGBM) en formato YAML o invocación de script.
*   Datos de entrenamiento: Batch extraído históricamente desde Feast Feature Store / S3 Feature Store.

## 9. Salidas
*   **Archivos:** Modelo entrenado (formato ONNX o Pickle), Gráficos SHAP (PNG/PDF).
*   **Metadatos:** Registros en la base de datos de MLflow de las métricas obtenidas.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Entrenamiento y versionado exitoso de un experimento
**Dado** que el Desarrollador (Tú) lanza un script de entrenamiento para el modelo de Predicción de Retrasos (v2.0)
**Cuando** el entrenamiento finaliza
**Entonces** el script envía las métricas (MAPE=12.5%) a MLflow
**Y** sube el archivo de modelo como artefacto a S3 gestionado por MLflow
**Y** registra la corrida vinculada al commit actual de Git, marcándola como completada.

### Escenario 2: Intento de promover un modelo deficiente a Producción
**Dado** que un modelo entrenado obtuvo un MAPE del 18.2%
**Cuando** el Desarrollador (Tú) intenta cambiar su estado (Tag) a `Production` en el Model Registry
**Entonces** el sistema de validación (CI/CD de ML) detecta que viola la regla RN-T05-001
**Y** bloquea la promoción, arrojando un error de validación de métricas.

## 11. Criterios de Aceptación
*   **CA-T05-001:** Cualquier modelo entrenado puede ser reproducido de manera idéntica ejecutando el mismo commit de código con el mismo Dataset ID proveniente de Feast Feature Store / S3.
*   **CA-T05-002:** El reporte SHAP es obligatorio; el entrenamiento falla a nivel de pipeline si no se logra generar la explicabilidad del modelo.

## 12. Restricciones
*   El entrenamiento de modelos pesados (Deep Learning, OCR) requiere provisión de nodos con aceleración GPU (NVIDIA T4 o superiores).

## 13. Fuera de Alcance
*   Monitoreo de deriva de datos (Data Drift) en inferencia real, eso pertenece al caso de uso operativo de evaluación (CU-O05). Este CU es netamente diseño y entrenamiento.

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Gestión de Secretos:** Las contraseñas y llaves de API se inyectarán de forma segura utilizando **GitHub Secrets** durante el pipeline de CI/CD, sin intervención manual en el panel del PaaS.
