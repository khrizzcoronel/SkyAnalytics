# Checklist de Validación: Módulo Operativo (QA / UAT)

Este documento contiene los criterios de aceptación y casos de prueba para validar la correcta implementación de los casos de uso **CU-O01 al CU-O20** (Capa Base / Backend Headless).

## 1. Requisitos Funcionales y Flujos Exitosos (Happy Paths)

### Ingesta de Datos y ETL (CU-O03, CU-O04)
- `[ ]` **CA-F01:** Verificar que el Cron Job en GitHub Actions (`daily-etl.yml`) arranca correctamente a las 02:00 AM.
- `[ ]` **CA-F02:** Verificar que el script Python extrae correctamente los datos de la fuente (Stripe API / PocketBase), los transforma y los inyecta masivamente (`Bulk Insert`) en MonetDB.
- `[ ]` **CA-F03:** Verificar que el Webhook de Stripe (`/api/v1/operativo/webhooks/stripe`) recibe correctamente el payload de un pago exitoso y actualiza PocketBase en tiempo real sin romper la firma criptográfica.

### Machine Learning y Backups (CU-O08, CU-O09, CU-O20)
- `[ ]` **CA-F04:** Verificar que el entrenamiento de Machine Learning (CU-O20) levanta una Instancia EC2 Spot, ejecuta el entrenamiento XGBoost, guarda el artefacto `.pkl` en el Bucket S3, y **se apaga automáticamente** al finalizar (Auto-Shutdown).
- `[ ]` **CA-F05:** Verificar que el volcado diario de base de datos (CU-O08/CU-O09) genera un archivo comprimido y lo transfiere de forma segura al Bucket S3 de respaldos.

## 2. Reglas de Negocio

- `[ ]` **CA-B01 (Cuarentena de Datos):** Inyectar intencionalmente una fila de datos corrupta (ej. un pago con importe negativo o string inválido). Verificar que el script ETL **no falla**, sino que envía la fila corrupta a la tabla `Quarantine_Data` en MonetDB y procesa el resto del lote normalmente.
- `[ ]` **CA-B02 (Ciclo de Vida S3):** Verificar en la consola de la nube que el Bucket de Modelos ML tiene configurada una regla de retención para mantener únicamente los últimos 3 checkpoints, eliminando los más antiguos (Control de Costos FinOps).

## 3. Escenarios de Error y Flujos Alternativos

- `[ ]` **CA-E01 (Fallo de Entrenamiento ML):** Forzar un error de Out of Memory (OOM) o de código en el script de Machine Learning. Verificar que la instancia Spot atrapa el error, envía una alerta a Sentry y **se apaga igualmente** para no generar cargos infinitos.
- `[ ]` **CA-E02 (Caída de Origen ETL):** Simular que la API de Stripe está caída durante la ventana de las 02:00 AM. Verificar que el flujo ETL hace al menos 3 reintentos (Retries) antes de abortar y notificar a los testers por Slack/Email.
- `[ ]` **CA-E03 (Error de Webhook):** Enviar un payload JSON inválido o con una firma incorrecta al Webhook de Stripe. Verificar que el endpoint retorna HTTP 401/400 de inmediato y no procesa datos.

## 4. Aspectos de Seguridad (Constitución)

- `[ ]` **CA-S01 (Zero Trust - Túnel ETL):** Comprobar los logs de ejecución de GitHub Actions. Verificar que el Runner no se conecta directamente a la IP pública de MonetDB, sino que levanta un **túnel efímero (SSH / Tailscale)** antes de enviar los datos, garantizando que el puerto de base de datos sigue cerrado al público.
- `[ ]` **CA-S02 (Cifrado de Backups):** Descargar el backup diario de S3. Intentar leerlo. Verificar que no es legible porque requiere una llave **AES-256** para ser desencriptado (Cifrado en reposo).
- `[ ]` **CA-S03 (Firma de Webhooks):** Interceptar el Webhook de Next.js. Verificar que el sistema valida estrictamente la cabecera criptográfica (`Stripe-Signature` o la de GitHub) contra un Secreto inyectado desde CI/CD.

## 5. Aspectos de Rendimiento y SLA

- `[ ]` **CA-P01 (ETL Batch Loading):** Inyectar un lote de prueba masivo (100,000 registros). Verificar que el script Python utiliza inserciones vectorizadas/masivas (`COPY INTO` o `Bulk Insert`) y completa la carga en MonetDB en **menos de 5 minutos**.
- `[ ]` **CA-P02 (Tiempo de Respuesta Webhook):** Enviar un evento al Webhook de Stripe. Verificar que el endpoint de Next.js acusa recibo (HTTP 200) en menos de **500ms**, derivando cualquier procesamiento pesado a una cola o ejecutándolo asíncronamente para evitar que Stripe haga reintentos innecesarios.
