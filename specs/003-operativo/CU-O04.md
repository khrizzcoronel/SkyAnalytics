# Especificación de Caso de Uso: CU-O04

## 1. Nombre de la Funcionalidad
**Validar Calidad de Datos en ETL**

## 2. Objetivo
Garantizar la integridad, precisión y conformidad del esquema (Data Contract) de los datos que ingresan a la plataforma mediante la ejecución automática de suites de aserciones estructurales y de negocio (Validaciones nativas (Pydantic/Zod)).

## 3. Actores Involucrados
*   **Actor Principal:** Desarrollador (Tú) / Sistema de Validación
*   **Sistemas Externos / Actores Secundarios:** Validaciones nativas (Pydantic/Zod), dbt, GitHub Actions (Cron) (Orquestador).

## 4. Contexto del Problema
El "Basura entra, basura sale" (Garbage In, Garbage Out) arruina los modelos de Machine Learning. Si la base de datos se llena con registros de vuelos sin identificador de aerolínea o con horas de llegada menores a la de salida (datos imposibles lógicamente), las predicciones fallarán y la confianza del cliente se perderá. La calidad debe probarse *antes* de que la data sea productiva.

## 5. Requisitos Funcionales
*   **RF-O04-001:** El sistema debe ejecutar la suite de Validaciones nativas (Pydantic/Zod) sobre los datos alojados en las tablas `Staging` inmediatamente después de la ingesta (CU-O03).
*   **RF-O04-002:** El sistema debe validar el "Data Contract": tipos de datos, presencia de columnas y nulidad permitida (ej. `flight_id` no puede ser NULL, `status` debe estar dentro del set ["SCHEDULED", "DELAYED", "CANCELLED"]).
*   **RF-O04-003:** El sistema debe ejecutar validaciones lógicas de negocio (ej. `arrival_time_utc` debe ser mayor estricto que `departure_time_utc`).
*   **RF-O04-004:** Si el porcentaje de registros fallidos ("Bad Records") supera el umbral de tolerancia (ej. 1%), todo el bloque de datos debe ser rechazado (Circuit Breaker).
*   **RF-O04-005:** Si la validación pasa, el DAG de GitHub Actions debe invocar a `dbt` para transformar e insertar los datos limpios en la capa Core (`Fact_Flight`).

## 6. Requisitos No Funcionales
*   **RNF-O04-001:** Las validaciones de Validaciones nativas (Pydantic/Zod) deben aprovechar el motor columnar subyacente (PocketBase (Operativa) y MonetDB (Analítica)) para ejecutar aserciones agregadas sobre millones de filas en menos de 2 minutos.
*   **RNF-O04-002:** Los resultados de validación (Data Docs) deben generarse como un sitio estático HTML y subirse a S3 para revisión humana de calidad.

## 7. Reglas de Negocio
*   **RN-O04-001 (Política de Circuit Breaker):** Una violación de llave primaria, de unicidad, o de nulo en columnas críticas (`PK`, `FK`) genera rechazo automático inmediato, deteniendo el flujo ETL hacia la capa productiva.
*   **RN-O04-002 (Cuarentena de Registros Flexibles):** Para violaciones en columnas no críticas (ej. falta de nombre de aeronave), el sistema aísla la fila defectuosa en una tabla de `quarantine` y deja pasar el resto, si el volumen de filas erróneas no supera el 5% del lote.

## 8. Entradas
*   Datos crudos alojados en tablas de esquema `staging` (PocketBase (Operativa) y MonetDB (Analítica)).
*   Definición de Expectativas (JSON/YAML suites de Validaciones nativas (Pydantic/Zod)).

## 9. Salidas
*   **Archivos:** Reporte HTML Data Docs subido a S3.
*   **Metadata:** Estado de la ejecución de la suite devuelta a GitHub Actions (Pass/Fail).
*   **Datos:** Registros promovidos (vía dbt) a la capa Core.

## 10. Escenarios (Formato Gherkin)

### Escenario 1: Validación 100% exitosa y promoción
**Dado** que los datos crudos del día se han cargado en `stg_flights`
**Cuando** el DAG ejecuta la tarea de Validaciones nativas (Pydantic/Zod)
**Entonces** se corren 50 aserciones de esquema y negocio
**Y** al arrojar 0 fallos, la tarea devuelve estado "Éxito"
**Y** `dbt` mueve e integra (UPSERT) de forma segura los datos limpios a la tabla de reportes final.

### Escenario 2: Interrupción del flujo por anomalía masiva (Schema Drift)
**Dado** que el proveedor externo eliminó la columna obligatoria `airline_code`
**Cuando** la suite de expectativas se ejecuta sobre la tabla staging
**Entonces** falla la aserción fundamental `expect_column_to_exist("airline_code")`
**Y** el pipeline se interrumpe instantáneamente mediante Circuit Breaker
**Y** los datos corruptos no manchan la tabla de hechos
**Y** el Desarrollador (Tú) recibe una alerta crítica con el reporte del fallo adjunto.

## 11. Criterios de Aceptación
*   **CA-O04-001:** La suite incluye aserciones estadísticas para detectar anomalías, como "El valor medio de `ticket_price` no puede desviarse más de 3 desviaciones estándar de la media histórica mensual".
*   **CA-O04-002:** Un fallo en validaciones bloqueantes jamás insertará ni una sola fila en el esquema principal de la base de datos (Transaccionalidad estricta).

## 12. Restricciones
*   La lógica de calidad de datos está abstraída en repositorios Git y sigue el mismo flujo CI/CD que el código de la aplicación.

## 13. Fuera de Alcance
*   Manejo y transformación de machine learning (Este caso de uso es 100% Desarrollador (Tú)ing).

## 14. Aclaraciones Globales (Speckit-Clarify)
*   **Errores ETL:** Si ingresan datos basura, se **aislarán en una tabla de cuarentena**, permitiendo que el resto del lote válido se cargue en la base de datos para no dejar vacíos los dashboards.
