# Especificación de Caso de Uso: CU-O03

## 1. Nombre de la Funcionalidad
**Ejecutar Ingesta Diaria de Datos**

## 2. Objetivo
Automatizar la extracción, carga inicial (Extract & Load - EL) y consolidación de lotes masivos de datos meteorológicos y aeronáuticos provenientes de proveedores externos hacia el Data Lake y el Data Warehouse.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Sistema (GitHub Actions (Cron))
*   **Sistemas Externos / Actores Secundarios:** Proveedores de Datos (OAG, NOAA), AWS S3 (Data Lake Raw), PocketBase (Operativa) y MonetDB (Analítica) (Data Warehouse).

## 4. Contexto del Problema
Los modelos predictivos y los dashboards requieren datos frescos y confiables. Cada madrugada, proveedores externos depositan archivos CSV y JSON gigantes (Terabytes) en servidores SFTP o buckets externos. SkyAnalytics debe descargar, descomprimir e ingerir esta data sin interrumpir las consultas analíticas en vivo (Zero-Downtime Data Load).

## 5. Requisitos Funcionales
*   **RF-O03-001:** GitHub Actions debe ejecutar tareas cronometradas (DAGs) a las 03:00 UTC para iniciar la descarga segura de archivos desde los SFTP/Buckets de los proveedores.
*   **RF-O03-002:** El sistema debe cargar los archivos crudos (Raw) directamente en particiones organizadas por fecha en un bucket S3 de Ingesta (`s3://sky-data-raw/oag/YYYY/MM/DD/`).
*   **RF-O03-003:** Tras la descarga, un proceso en memoria (Spark/Pandas) debe estandarizar los formatos de fecha a ISO 8601 y normalizar la codificación a UTF-8.
*   **RF-O03-004:** Los datos normalizados deben cargarse en tablas `Staging` temporales dentro del Data Warehouse (PocketBase (Operativa) y MonetDB (Analítica)) usando procesos de carga masiva rápida (COPY INTO).
*   **RF-O03-005:** Al finalizar, el DAG debe reportar su estado (Success/Failed) a la consola de observabilidad.

## 6. Requisitos No Funcionales
*   **RNF-O03-001 (Performance):** La carga masiva de un lote de 10 GB de archivos CSV crudos hacia la tabla Staging no debe tomar más de 15 minutos en total.
*   **RNF-O03-002 (Idempotencia):** El DAG debe ser 100% idempotente. Si falla a la mitad y se reejecuta, no debe duplicar las filas ni corromper los datos del día anterior.

## 7. Reglas de Negocio
*   **RN-O03-001 (Aislamiento de Staging):** Jamás se debe insertar directamente en la tabla principal (`Fact_Flight`). Todo pasa por la capa de `Staging` donde ocurrirá la validación de calidad (CU-O04).
*   **RN-O03-002 (Retry Policy):** Si el servidor SFTP del proveedor no responde (Connection Timeout), GitHub Actions intentará 3 veces con un retroceso exponencial (Exponential Backoff) de 5, 10 y 20 minutos antes de declarar el DAG como Fallido.

## 8. Entradas
*   Archivos comprimidos (ZIP/GZ) conteniendo CSV/JSON provistos por OAG (Vuelos) o NOAA (Clima).
*   Configuración del DAG en Python.

## 9. Salidas
*   Archivos crudos persistidos en Data Lake S3.
*   Tablas `Staging` pobladas en PocketBase (Operativa) y MonetDB (Analítica).
*   Estado de la tarea emitido por GitHub Actions.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Ingesta nocturna exitosa
**Dado** que son las 03:00 UTC y el archivo `daily_flights_20261102.csv.gz` está listo en el SFTP
**Cuando** el DAG de Ingesta OAG se dispara
**Entonces** el archivo se transfiere al bucket S3 Raw exitosamente
**Y** los datos se desempaquetan y normalizan
**Y** se realiza el `COPY INTO` masivo hacia la tabla `stg_oag_flights` en 4 minutos
**Y** el DAG marca la tarea como exitosa.

### Escenario 2: Proveedor externo inaccesible
**Dado** que el proveedor NOAA sufre una caída de sus servidores SFTP
**Cuando** el DAG intenta realizar la conexión inicial
**Entonces** la conexión hace Timeout
**Y** GitHub Actions reintenta 3 veces esperando entre cada intento
**Y** al agotar los intentos, falla y envía una Alerta Naranja (Sev2) a Slack notificando que la ingesta del clima está retrasada.

## 11. Criterios de Aceptación
*   **CA-O03-001:** Archivos mal formados que causen errores de sintaxis durante el COPY INTO (ej. separadores incorrectos) son movidos automáticamente a una carpeta `s3://sky-data-raw/quarantine/` sin abortar el procesamiento de los demás archivos.
*   **CA-O03-002:** El conteo de filas del archivo origen (CSV) y de la tabla de staging poblada deben ser exactamente el mismo.

## 12. Restricciones
*   El proceso de extracción de archivos no debe consumir el ancho de banda dedicado a las API del usuario final (las descargas ocurren en VPCs y subredes dedicadas).

## 13. Fuera de Alcance
*   Limpieza semántica y cruces lógicos complejos de los datos (Esto corresponde al proceso de Transformación de dbt, que ocurre después de la carga inicial).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Errores ETL:** Si ingresan datos basura, se **aislarán en una tabla de cuarentena**, permitiendo que el resto del lote válido se cargue en la base de datos para no dejar vacíos los dashboards.
