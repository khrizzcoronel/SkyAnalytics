# Especificación de Caso de Uso: CU-O21

## 1. Nombre de la Funcionalidad
**Ejecutar ETL de flights_raw a MonetDB (Star Schema)**

## 2. Objetivo
Extraer, transformar y cargar incrementalmente los registros cargados en la base de datos operativa `flights_raw` de PocketBase hacia el Data Warehouse columnar de MonetDB, estructurando la información bajo un diseño dimensional en estrella (Star Schema) para maximizar la velocidad de las consultas de negocio y telemetría.

## 3. Actores Involucrados
- **Actor Principal:** GitHub Actions (Cron) / Sistema
- **Sistemas Secundarios:** PocketBase (SQLite), MonetDB

## 4. Contexto del Problema
PocketBase aloja los registros crudos de vuelos en `flights_raw`. Para realizar analítica compleja (retrasos agregados, promedios mensuales por aerolínea y visualización BSC), estos registros deben estructurarse de forma óptima. Esto requiere un proceso de transformación diario (ETL) que normalice las dimensiones y alimente una tabla de hechos (`fact_flights`).

## 5. Requisitos Funcionales
- **RF-O21-001:** El pipeline debe activarse a las 03:00 AM todos los días.
- **RF-O21-002:** Debe extraer los datos desde PocketBase.
- **RF-O21-003:** Debe generar y mantener las dimensiones `dim_airline`, `dim_airport` y `dim_date`.
- **RF-O21-004:** Debe consolidar los registros en la tabla de hechos `fact_flights` de MonetDB.
- **RF-O21-005:** Debe refrescar automáticamente las vistas materializadas `vw_bsc_monthly` y `vw_delay_analysis`.

## 6. Requisitos No Funcionales
- **RNF-O21-001 (Performance):** La carga completa e incremental debe resolverse en menos de 5 minutos.
- **RNF-O21-002 (Idempotencia):** El proceso debe ser 100% re-ejecutable sin duplicar registros.

## 7. Escenarios (Gherkin)

### Escenario 1: Ingesta ETL Diaria Exitosa
- **DADO** que son las 03:00 AM y el importador cargó nuevos registros en `flights_raw`
- **CUANDO** el pipeline de transformación se dispara
- **ENTONCES** extrae las filas, normaliza las dimensiones e inserta masivamente en `fact_flights`
- **Y** refresca las vistas de MonetDB con éxito.

## 8. Reglas de Negocio
- **RN-O21-001 (Incrementalidad):** El ETL debe usar el watermark `MAX(pb_created)` de `fact_flights` para procesar únicamente registros nuevos de `flights_raw`.
- **RN-O21-002 (Cuarentena):** Las filas que fallen las reglas de `DataValidator` deben insertarse en la tabla `Quarantine_Data` de MonetDB sin abortar el pipeline.
- **RN-O21-003 (Refresco de vistas):** Las vistas `vw_bsc_monthly` y `vw_delay_analysis` deben recrearse solo después de que `fact_flights` y las dimensiones se hayan cargado exitosamente.

## 9. Entradas
| Campo | Tipo | Descripción |
|---|---|---|
| `flights_raw` | Tabla PocketBase | Registros crudos de vuelos importados por `CU-O22`. |
| `fact_flights.pb_created` | TIMESTAMP | Watermark para carga incremental. |
| `MONETDB_*` | Env vars | Credenciales de conexión a MonetDB. |

## 10. Salidas
| Campo / Objeto | Tipo | Descripción |
|---|---|---|
| `dim_airline` | Tabla MonetDB | Dimensión de aerolíneas. |
| `dim_airport` | Tabla MonetDB | Dimensión de aeropuertos. |
| `dim_date` | Tabla MonetDB | Dimensión de fechas. |
| `fact_flights` | Tabla MonetDB | Tabla de hechos con claves sustitutas. |
| `vw_bsc_monthly` | Vista MonetDB | Agregados mensuales para BSC. |
| `vw_delay_analysis` | Vista MonetDB | Vista plana para ML/drift. |
| `Quarantine_Data` | Tabla MonetDB | Registros corruptos con `quarantine_reason`. |

## 11. Criterios de Aceptación
- **CA-O21-001:** El cronjob `etl-flights.yml` arranca a las 03:00 AM UTC y el ETL finaliza sin errores.
- **CA-O21-002:** Re-ejecutar el ETL inmediatamente después de una corrida exitosa no duplica registros en `fact_flights`.
- **CA-O21-003:** Inyectar 5 filas corruptas (ej. `distance <= 0`) resulta en 5 registros en `Quarantine_Data` y el resto se carga normalmente.

## 12. Restricciones
- Requiere que `flights_raw` esté poblada previamente (`CU-O22`).
- MonetDB debe estar disponible y accesible con credenciales configuradas.
- El proceso debe ejecutarse con privilegios de escritura en las tablas de MonetDB.

## 13. Fuera de Alcance
- Limpieza o re-procesamiento manual de `Quarantine_Data` (se define en `CU-O04`).
- Reentrenamiento automático del modelo ML (`CU-O05`).
- Notificaciones Slack por fallos del ETL (`CU-O10` / `CU-O13`).

## 14. Aclaraciones Globales (Speckit-Clarify)
- **Tolerancia a fallos parciales:** Datos corruptos van a cuarentena; el pipeline no falla por filas aisladas.

