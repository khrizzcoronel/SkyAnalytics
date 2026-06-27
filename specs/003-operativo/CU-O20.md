# Especificación de Caso de Uso: CU-O20

## 1. Nombre de la Funcionalidad
**Ejecutar Experimentos de Deep Learning**

## 2. Objetivo
Proveer al equipo de Desarrollador (Tú)s y Data Scientists un entorno especializado, escalable (GPU/TPU) y versionado para la investigación y experimentación con redes neuronales complejas (Deep Learning, ej. modelos multimodales, procesamiento de lenguaje natural o visión computacional) sin afectar la infraestructura transaccional de SkyAnalytics.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** Entorno local o Google Colab / PaaS GPU Node Pools, Ray (Computación Distribuida), Tracking básico o local.

## 4. Contexto del Problema
A diferencia del entrenamiento rutinario de algoritmos de Machine Learning tabulares (CU-O05 - XGBoost), los experimentos con arquitecturas Deep Learning masivas (como modelos de NLP para procesar NOTAMs o Whisper para analizar comunicaciones de control de tráfico aéreo) exigen cómputo distribuido intensivo. Si un experimento consume demasiada memoria de la base de datos o congestiona la red, puede tirar la plataforma.

## 5. Requisitos Funcionales
*   **RF-O20-001:** El sistema debe permitir al Desarrollador (Tú) aprovisionar el entorno de entrenamiento mediante un flujo simple (ej. GitHub Actions manual `workflow_dispatch`) que levante una única instancia GPU (AWS EC2 Spot), clonando automáticamente la rama de experimentación desde GitHub.
*   **RF-O20-002:** El sistema debe leer grandes volúmenes de datos no estructurados (ej. audios de torres de control en S3, textos libres) saltándose el Data Warehouse tabular (PocketBase (Operativa) y MonetDB (Analítica)) para evitar sobrecarga del entorno OLAP, conectándose directamente al Data Lake (S3).
*   **RF-O20-003:** El sistema debe realizar un *checkpointing* automático (guardado del estado de los tensores/pesos del modelo) cada 10 epochs (por defecto) o cada hora de procesamiento, conservando únicamente los últimos 3 checkpoints en S3 para minimizar costos de almacenamiento.
*   **RF-O20-004:** El sistema debe integrar la telemetría del entrenamiento de la red neuronal profunda (TensorBoard / Tracking básico o local) para monitorear las curvas de pérdida (Loss curves) y prevenir sobreajuste (Overfitting).

## 6. Requisitos No Funcionales
*   **RNF-O20-001 (Aislamiento de Cómputo):** Los pods o instancias de experimentación GPU deben correr en una subred de PaaS estrictamente aislada (Node Taints/Tolerations) que garantice que ningún microservicio de API crítica intente ser programado en esos nodos costosos y ruidosos.
*   **RNF-O20-002 (Control de Costos):** El entorno debe auto-destruirse al finalizar el script de entrenamiento de forma determinista (Job-based execution). Como red de seguridad, un demonio interno evaluará el uso combinado de CPU y GPU; si ambos caen por debajo del 5% durante 30 minutos, la instancia se apagará forzosamente para proteger el presupuesto personal.

*   **RNF-O20-003 (Protección de Presupuesto / Fallback):** Si AWS no dispone de instancias Spot solicitadas (Insuficient Capacity), el flujo debe abortar de inmediato y notificar por Slack, quedando estrictamente prohibido el escalado automático a instancias On-Demand (pago completo).
## 7. Reglas de Negocio
*   **RN-O20-001 (Ciclo de Vida de Investigación):** Los experimentos de Deep Learning generan un artefacto de prueba de concepto (PoC, ej. Jupyter Notebook renderizado en HTML). Este artefacto se adjunta a un Pull Request en GitHub. La aprobación (Merge) del PR actúa como la validación formal para simular la "aprobación del Desarrollador (Tú)".

## 8. Entradas
*   Código de modelo inyectado automáticamente al iniciar la instancia (Git Clone vía UserData script).
*   Datos crudos multimedia/texto (S3).
*   Parámetros de entrenamiento (Epochs, Batch Size, Learning Rate).

## 9. Salidas
*   Pesos del Modelo Deep Learning (`.pt` o `.h5`).
*   Checkpoints serializados a S3.
*   Dashboards de TensorBoard incrustados en Tracking básico o local UI.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Entrenamiento distribuido exitoso y Checkpointing
**Dado** que el Desarrollador (Tú) lanza un experimento para procesar 1 millón de notas NOTAM usando un modelo Transformers
**Cuando** el orquestador solicita 4 nodos AWS de tipo `p4d.24xlarge` (GPU)
**Entonces** el entrenamiento comienza de forma distribuida (Data Parallelism)
**Y** después de finalizar el Epoch 50
**Y** el sistema guarda el Checkpoint de los pesos del modelo en el bucket S3 para asegurar el progreso
**Y** actualiza en tiempo real las métricas de Pérdida de Entrenamiento (Training Loss) en Tracking básico o local.

### Escenario 2: Destrucción automática por inactividad
**Dado** que el Desarrollador (Tú) terminó de correr un experimento el viernes en la noche
**Cuando** el script de entrenamiento termina y no se encolan más tareas en el nodo de GPU
**Entonces** el monitor de hardware detecta inactividad (Idle) durante 60 minutos
**Y** desaprovisiona el nodo `p4d.24xlarge` costoso del clúster
**Y** notifica al Desarrollador (Tú) que el entorno experimental ha sido apagado por razones financieras.

## 11. Criterios de Aceptación
*   **CA-O20-001:** La interrupción de una instancia Spot a la mitad de un experimento no corrompe el entrenamiento; un nuevo nodo debe ser capaz de levantar el último Checkpoint y reanudar el entrenamiento matemático sin intervención humana.

## 12. Restricciones
*   Toda extracción masiva de datos (Dataloaders en PyTorch) hacia las GPUs debe cursarse a través de Endpoints VPC (PrivateLink) de AWS para S3, impidiendo que el volumen masivo de tráfico salga a internet y genere costos astronómicos de transferencia de datos (Egress Costs).

## 13. Fuera de Alcance
*   Servicio de inferencia de baja latencia del modelo Deep Learning (Desplegar estos modelos en producción para contestar en 50ms exige optimización ONNX/TensorRT e infraestructura dedicada, lo cual no es parte del experimento inicial).
