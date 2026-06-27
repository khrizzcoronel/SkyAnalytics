# Especificación de Caso de Uso: CU-T04

## 1. Nombre de la Funcionalidad
**Monitorear Pipelines ETL y Calidad**

## 2. Objetivo
Otorgar al Desarrollador (Tú) visibilidad completa sobre los procesos de Ingesta, Transformación y Carga (ETL) orquestados por GitHub Actions y transformados con dbt, asegurando la calidad (Validaciones nativas (Pydantic/Zod)) y la frescura de los datos aeronáuticos.

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú)
*   **Sistemas Externos / Actores Secundarios:** GitHub Actions (Cron), dbt, Validaciones nativas (Pydantic/Zod), Slack (Alertas).

## 4. Contexto del Problema
SkyAnalytics ingesta terabytes de información de vuelos, radar y clima de proveedores externos diariamente. Si un proveedor envía un esquema modificado (schema drift), datos nulos en campos clave, o los pipelines se retrasan, los dashboards y predicciones fallarán, violando el acuerdo de frescura ($<$ 5 min).

## 5. Requisitos Funcionales
*   **RF-T04-001:** El sistema debe proporcionar un dashboard (vía GitHub Actions UI) que muestre el estado en tiempo real (Success, Running, Failed, Queued) de todos los DAGs (Directed Acyclic Graphs).
*   **RF-T04-002:** El sistema debe capturar el resultado de las suites de validación de **Validaciones nativas (Pydantic/Zod)** (Data Quality) insertadas como nodos dentro del DAG de GitHub Actions.
*   **RF-T04-003:** Si un Data Contract (esquema o restricción) se rompe durante la ingesta, el sistema debe detener la propagación de esos datos corruptos a PocketBase (Operativa) y MonetDB (Analítica).
*   **RF-T04-004:** El sistema debe alertar proactivamente por Slack al canal de `#data-ops` si un DAG falla o si una validación de calidad crítica no pasa.
*   **RF-T04-005:** El sistema debe calcular y mostrar el lag de frescura (Data Freshness) comparando el timestamp de los últimos datos ingestados con la hora actual.

## 6. Requisitos No Funcionales
*   **RNF-T04-001:** El monitoreo no debe imponer sobrecarga de procesamiento en los workers de transformación; las validaciones deben correr en paralelo o en el momento exacto post-transformación (`dbt test`).
*   **RNF-T04-002:** Todos los logs de los pipelines ETL deben ser retenidos y accesibles (Archivos de Log/Elasticsearch) por al menos 90 días por motivos de auditoría SOC 2.

## 7. Reglas de Negocio
*   **RN-T04-001 (Severidad de Alertas):**
    *   *Warning:* Retraso en la finalización de un DAG superior al 20% de su tiempo histórico.
    *   *Critical:* Falla total del DAG o corrupción detectada en tablas dimensionales clave (Vuelos, Aeropuertos).
*   **RN-T04-002 (Circuit Breaker de Datos):** Ningún dato que falle la prueba de nulos en `flight_id` o `departure_time` puede ser consolidado en la tabla de hechos.

## 8. Entradas
*   Eventos de estado de tareas (Task Instances) desde el orquestador GitHub Actions.
*   Resultados de ejecución generados por dbt (`run_results.json`) y Validaciones nativas (Pydantic/Zod).

## 9. Salidas
*   **Alertas:** Mensajes en formato enriquecido (bloques JSON) hacia Slack/Notificaciones de Slack con el link directo a los logs del error.
*   **UI (Data Observability Dashboard):** Vistas del estado y linaje de datos.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Ejecución limpia y validación de calidad
**Dado** que el pipeline de ingesta horaria de OAG Flight Data se activa
**Cuando** el DAG extrae y carga (EL) los datos crudos
**Y** dbt ejecuta las transformaciones y pruebas de calidad (Validaciones nativas (Pydantic/Zod))
**Entonces** todas las expectativas pasan exitosamente
**Y** los datos se fusionan con la base de datos principal (PocketBase (Operativa) y MonetDB (Analítica))
**Y** el dashboard marca el DAG como "Success" y actualiza la frescura a "0 minutos".

### Escenario 2: Detección y contención de Schema Drift (Circuit Breaker)
**Dado** que el proveedor externo cambia el nombre de la columna `delay_minutes` por `delay_min` sin avisar
**Cuando** el DAG intenta procesar la tabla cruda
**Entonces** la prueba de esquema estructural falla
**Y** el sistema detiene inmediatamente el pipeline, aislando los datos corruptos en cuarentena (Staging)
**Y** envía una alerta crítica a Slack indicando "Schema Drift detectado en OAG Feed".

## 11. Criterios de Aceptación
*   **CA-T04-001:** La alerta en Slack debe generarse en menos de 1 minuto tras la falla de un nodo del pipeline.
*   **CA-T04-002:** El linaje de los datos debe poder trazarse desde la tabla de destino (PocketBase (Operativa) y MonetDB (Analítica)) hasta la tabla origen (Raw S3) para facilitar el debug.

## 12. Restricciones
*   La lógica de transformación de dbt debe ser idempotente, permitiendo que un DAG fallido pueda re-ejecutarse (backfill) sin duplicar filas en la tabla de hechos.

## 13. Fuera de Alcance
*   Creación de nuevos conectores de bases de datos desde esta interfaz (El código ETL se hace en repositorios Git y se despliega vía CI/CD).
