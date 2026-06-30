# Tareas de Implementación: Módulo Operativo

Este documento define la secuencia lógica de desarrollo para construir la Capa de Trabajo Pesado (ETL, Webhooks, Machine Learning - CU-O01 a CU-O20). Este módulo no tiene UI, por lo que las tareas se enfocan en infraestructura, scripts de Python y orquestación.

---

## FASE 1: Infraestructura y Seguridad (Zero Trust)

### TASK-O01: Cifrado de Volumen y Túnel Seguro
*   **Descripción:** Configurar el cifrado de volumen completo (AES-256 vía LUKS o AWS EBS) en la VPS que aloja a PocketBase y MonetDB. Además, instalar Tailscale (o configurar un Túnel SSH) para que los puertos de las bases de datos no estén expuestos a la internet pública (Zero Trust).
*   **Requisitos:** CA-S01, CA-S02, Constitución (Seguridad).
*   **Dependencias:** VPS aprovisionada (TASK-002 del Módulo Estratégico).
*   **Criterio de Completado:** Un escáner de puertos público (Nmap) contra la IP de la VPS muestra los puertos de base de datos como "Closed/Filtered", pero se puede acceder vía la IP privada de Tailscale.

### TASK-O02: Aprovisionar Buckets en S3
*   **Descripción:** Crear en AWS S3 (o R2/MinIO) los buckets: `skyanalytics-db-backups` y `skyanalytics-ml-models`. Configurar una Política de Ciclo de Vida (*Lifecycle Policy*) en el bucket de modelos para eliminar archivos de más de 30 días, reteniendo solo los últimos checkpoints.
*   **Requisitos:** CA-B02, FinOps.
*   **Dependencias:** Ninguna.
*   **Criterio de Completado:** Los buckets existen y tienen políticas de expiración activas.

---

## FASE 0: Carga Semilla y Procesamiento de Vuelos (Nuevo Core)

### TASK-O00-A: Implementar Servicio Docker de Seed Import (CU-O22)
*   **Descripción:** Crear `backend/import/import_flights.py` que importe `flight_data_2024.csv` en lotes de 100K registros de forma reanudable (checkpoint).
*   **Criterio de Completado:** Ejecutar el contenedor importa las primeras 100K filas y guarda el checkpoint.

### TASK-O00-B: Implementar ETL de PocketBase a MonetDB (CU-O21)
*   **Descripción:** Crear `etl_flights_to_monetdb.py` que transforme `flights_raw` de PocketBase a dimensiones y hechos en MonetDB.
*   **Criterio de Completado:** Los datos procesados se cargan correctamente en MonetDB y refrescan las vistas.

### TASK-O00-C: Implementar Feature Engineering Pipeline (CU-O24)
*   **Descripción:** Crear `feature_engineering.py` para calcular variables del modelo XGBoost y guardarlas en Parquet en S3.

## FASE 2: Ingesta de Datos (ETL y Cuarentena)

### TASK-O03: Implementar Tabla de Cuarentena en MonetDB
*   **Descripción:** Crear la tabla `Quarantine_Data` en MonetDB. Esta tabla almacenará registros basura o incompletos desviados por el proceso ETL para su revisión manual.
*   **Requisitos:** Directriz Global (Tolerancia a fallos parciales).
*   **Dependencias:** TASK-O01
*   **Criterio de Completado:** La tabla existe y acepta inserciones.

### TASK-O04: Desarrollar Pipeline ETL en Python
*   **Descripción:** Escribir el script `EtlPipeline.py` usando Pandas o Polars. Debe extraer datos (ej. simular API de Stripe), validarlos y utilizar un conector nativo (ej. `pymonetdb`) para inyectarlos en la Fact Table. Debe tener la lógica condicional para desviar datos corruptos a `Quarantine_Data` en lugar de crashear (CA-B01).
*   **Requisitos:** CA-F02, CA-B01
*   **Dependencias:** TASK-O03
*   **Criterio de Completado:** Ejecutar `python EtlPipeline.py` procesa 1,000 registros, insertando 995 en la tabla principal y 5 corruptos en Cuarentena sin detener el proceso.

---

## FASE 3: Orquestación Serverless y Machine Learning

### TASK-O05: Configurar Trabajos Cron en GitHub Actions
*   **Descripción:** Crear el archivo `.github/workflows/daily-etl.yml` que defina un Cron Job (`0 2 * * *`). Este Action debe configurar el túnel seguro (Tailscale Action), inyectar los secretos de base de datos y ejecutar el script `EtlPipeline.py`.
*   **Requisitos:** CA-F01, CA-S01
*   **Dependencias:** TASK-O04
*   **Criterio de Completado:** El pipeline corre exitosamente en GitHub Actions simulando las 02:00 AM y los datos aparecen en MonetDB.

### TASK-O06: Desarrollar Script de ML Epímero (Instancia Spot)
*   **Descripción:** Escribir `MlTrainer.py` usando XGBoost. El script entrena el modelo predictivo, sube el `.pkl` a S3 (TASK-O02) usando Boto3, y ejecuta `os.system('shutdown -h now')` al terminar (o atrapar una excepción) para ahorrar dinero.
*   **Requisitos:** CA-F04, CA-E01 (Auto-Shutdown)
*   **Dependencias:** TASK-O02
*   **Criterio de Completado:** Lanzar la instancia en AWS resulta en la creación del modelo en S3 y la destrucción inmediata de la instancia.

---

## FASE 4: Webhooks en Tiempo Real (Next.js)

### TASK-O07: Implementar Webhook de Stripe
*   **Descripción:** En el backend de Next.js, crear la ruta `/api/v1/operativo/webhooks/stripe`. Esta ruta debe validar obligatoriamente la firma criptográfica (`Stripe-Signature`), retornar HTTP 200 rápido y actualizar asíncronamente PocketBase si el pago falló (para suspender la cuenta).
*   **Requisitos:** CA-F03, CA-S03, CA-P02 (Tiempo de respuesta < 500ms).
*   **Dependencias:** TASK-T01 (Metadatos en PocketBase).
*   **Criterio de Completado:** Enviar un evento falso vía Stripe CLI retorna un 200 OK y PocketBase refleja la suspensión del cliente moroso.
