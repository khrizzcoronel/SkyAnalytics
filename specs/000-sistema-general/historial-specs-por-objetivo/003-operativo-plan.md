# Diseño Técnico: Módulo Operativo

## 1. Arquitectura de la Solución (Capa de Carga de Trabajo y ETL)
**Patrón Arquitectónico:** Serverless Event-Driven & Trabajos Cron (Headless).
Este módulo agrupa los casos de uso **CU-O01 al CU-O20**. A diferencia de los módulos Estratégico y Táctico, este módulo **no posee Interfaz de Usuario (UI)**. Es el motor "invisible" (Backend profundo) que extrae, procesa y sirve los datos para todo el ecosistema SkyAnalytics.

*   **Orquestación de Procesos (Scheduler):** En lugar de herramientas pesadas como Apache Airflow, se utilizarán **GitHub Actions (Cron Triggers)** para programar y ejecutar los pipelines de datos (ETL) diarios y tareas de mantenimiento.
*   **Procesamiento de Datos (ETL):** Scripts en **Python (Pandas / Polars)** ejecutados dentro de los *runners* de GitHub Actions. Extraen datos de las fuentes (Stripe, APIs, Base transaccional), los limpian y los cargan en MonetDB.
*   **Procesamiento Pesado (Machine Learning - CU-O20):** Para entrenamientos de Modelos (XGBoost/PyTorch), GitHub Actions disparará (mediante AWS CLI/Boto3) una **Instancia EC2 Spot con GPU**, pasándole el código mediante `UserData` (Git clone al inicio). Al terminar el script, la instancia se auto-destruye para proteger el presupuesto.

## 2. Modelo de Base de Datos (Ingesta y Almacenamiento)

### 2.1 Tablas Analíticas (MonetDB - Star Schema)
El objetivo principal del módulo operativo es mantener estas tablas maestras actualizadas, inyectando millones de filas optimizadas por lotes (*Batch Loading*):
*   **`fact_flights`**: Tabla de hechos principal (7.08M registros) con todas las columnas del dataset BTS (incluyendo campos extras para features) y claves foráneas a las dimensiones.
*   **`dim_airline`**: Dimension table con los códigos e identificadores de aerolíneas.
*   **`dim_airport`**: Dimension table para códigos IATA de aeropuertos, ciudades y estados (origen/destino).
*   **`dim_date`**: Dimension table de tiempo para facilitar agregados cronológicos.
*   **`Fact_Suscripcion` / `Fact_Billing`**: Ingresos de clientes (SaaS metrics complementarias).
*   **`Fact_API_Call`**: Telemetría de uso del sistema.
*   **`Quarantine_Data`**: Tabla arquitectónica donde el ETL envía las filas del dataset corruptas o anómalas (aislamiento del Circuit Breaker).

### 2.2 Almacenamiento de Objetos (S3 Compatible)
*   **`Bucket: Modelos-ML`**: Almacenamiento para los artefactos de Machine Learning (archivos `.pkl` o `.onnx`) generados por el CU-O20. Se limitará el ciclo de vida para retener solo los últimos 3 checkpoints (Ahorro de costos).
*   **`Bucket: Backups-DB`**: Almacenamiento cifrado (AES-256) para los volcados de base de datos diarios generados por el caso de uso de respaldo.

## 3. Endpoints (Webhooks Operativos)
Aunque la mayoría son trabajos *Cron*, se expondrán webhooks protegidos en Next.js (`/api/v1/operativo/*`) para escuchar eventos del exterior:

| Método | Ruta | Descripción | Seguridad |
| :--- | :--- | :--- | :--- |
| `POST` | `/webhooks/stripe` | Escucha pagos fallidos/exitosos para actualizar PocketBase al instante. | Validación de Firma Criptográfica (Stripe Secret) |
| `POST` | `/webhooks/github` | Trigger para ejecutar auto-despliegues al detectar un `Push` en la rama `main`. | Token (GitHub Secret) |
| `POST` | `/ml/callback` | Recibe la notificación de la instancia Spot informando que el entrenamiento de ML terminó exitosamente. | Token Fijo de Infraestructura |

## 4. Componentes y Clases Principales (Core Lógico)

### 4.1 Scripts Python (ETL y ML)
*   **`EtlPipeline.py`:** Orquestador del flujo ETL. Cuenta con funciones `extract()`, `transform()` (con validación nativa de tipos) y `load_to_monetdb()` (utilizando inserciones masivas `COPY INTO`).
*   **`DataValidator.py`:** Implementa lógica condicional. Si una fila de datos no coincide con el esquema, la separa y la enruta a la tabla de `Quarantine_Data`.
*   **`MlTrainer.py`:** Script agnóstico que entrena un modelo XGBoost, evalúa la precisión, guarda el binario en S3 y se apaga automáticamente (`os.system('shutdown -h now')`).

### 4.2 Lógica en Bash/YAML
*   **`.github/workflows/daily-etl.yml`:** Archivo que levanta un contenedor Python y ejecuta `EtlPipeline.py` todos los días a las 02:00 AM.
*   **Seguridad Zero Trust (Túnel SSH/Tailscale):** Antes de ejecutar el script Python, el *runner* de GitHub Actions levantará un túnel cifrado efímero (vía SSH o Tailscale) hacia la VPS. Esto evita tener que exponer el puerto 50000 de MonetDB al internet público.

## 5. Flujo de Datos Global (Ejemplo: Ingesta ETL - CU-O03)
1.  **Disparador:** GitHub Actions inicia el flujo `daily-etl.yml` a las 02:00 AM.
2.  **Extracción:** `EtlPipeline.py` se conecta vía API a las fuentes (Ej. Stripe Test Mode).
3.  **Limpieza:** Se detectan 5 filas con `monto_pago` nulo. El script las desvía a `Quarantine_Data`. El resto del bloque (1,000 filas) pasa la validación.
4.  **Carga (Load):** Se abre una conexión ODBC rápida hacia MonetDB y se hace un volcado (`Bulk Insert`) a `Fact_Billing`.
5.  **Cierre:** Si hubo error crítico, el script Python retorna `exit(1)` y GitHub Actions notifica a Sentry. Si fue exitoso, el *runner* se apaga y el trabajo se marca como verde.

## 6. Dependencias con Otros Módulos
*   **Impacto Total:** Este módulo es la base del sistema. Los tableros del Módulo Estratégico (ARR, Uptime, BSC) **son inútiles sin este módulo**, ya que consumen exclusivamente los datos que el Módulo Operativo procesa y guarda en MonetDB.

## 7. Decisiones Técnicas y Justificación
*   **GitHub Actions como Orquestador (en lugar de Airflow):** 
    *   *Por qué:* Instalar y mantener un servidor Apache Airflow 24/7 requiere pagar instancias robustas mensualmente. GitHub Actions ofrece miles de minutos gratuitos mensuales y servidores efímeros que no cuestan nada cuando no corren código, perfecto para un proyecto personal.
*   **Desacople Completo de Machine Learning (Instancias Spot):** 
    *   *Por qué:* Ejecutar cargas de Inteligencia Artificial en el mismo servidor web que aloja Next.js o la API colapsaría la memoria de la aplicación, causando caída total del servicio (Out Of Memory). Levantar una instancia Spot remota, entrenar y apagarla inmediatamente previene interrupciones y reduce los costos a centavos de dólar.
*   **Aislamiento de Cuarentena (Tolerancia a fallos):** 
    *   *Por qué:* Previene que un solo dato mal formateado detenga la carga de millones de registros (Fallar suavemente). El Desarrollador puede revisar luego por qué falló ese registro específico.
*   **Cifrado a Nivel de Volumen (AES-256):**
    *   *Por qué:* Las bases de datos operativas (PocketBase) y analíticas (MonetDB) guardan los datos en texto plano en el disco de la VPS. Para cumplir con la Constitución, el disco completo de la VPS estará cifrado con LUKS o EBS Encryption, garantizando el cifrado en reposo sin necesidad de modificar el código de la aplicación.
