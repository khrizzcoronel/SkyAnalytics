# Checklist de Validación: Data Pipeline

## CU-O03 — Ejecutar Ingesta Diaria de Datos
- [ ] **CA-O03-001:** Archivos mal formados que causen errores de sintaxis durante el COPY INTO (ej. separadores incorrectos) son movidos automáticamente a una carpeta `s3://sky-data-raw/quarantine/` sin abortar el procesamiento de los demás archivos.
- [ ] **CA-O03-002:** El conteo de filas del archivo origen (CSV) y de la tabla de staging poblada deben ser exactamente el mismo.

## CU-O04 — Validar Calidad de Datos en ETL
- [ ] **CA-O04-001:** La suite incluye aserciones estadísticas para detectar anomalías, como "El valor medio de `ticket_price` no puede desviarse más de 3 desviaciones estándar de la media histórica mensual".
- [ ] **CA-O04-002:** Un fallo en validaciones bloqueantes jamás insertará ni una sola fila en el esquema principal de la base de datos (Transaccionalidad estricta).

## CU-O17 — Validar Data Contracts en Pipeline ETL
- [ ] **CA-O17-001:** El equipo Consumidor (desarrolladores) debe ser notificado automáticamente por correo/Slack 30 días antes de que un equipo Productor ejecute una migración planificada de un "Breaking Change" (Deprecation Plan).

## CU-O21 — Ejecutar ETL de flights_raw a MonetDB (Star Schema)
- [ ] **CA-O21-001:** El cronjob `etl-flights.yml` arranca a las 03:00 AM UTC y el ETL finaliza sin errores.
- [ ] **CA-O21-002:** Re-ejecutar el ETL inmediatamente después de una corrida exitosa no duplica registros en `fact_flights`.
- [ ] **CA-O21-003:** Inyectar 5 filas corruptas (ej. `distance <= 0`) resulta en 5 registros en `Quarantine_Data` y el resto se carga normalmente.

## CU-O22 — Importar Dataset flights_raw de forma Incremental
- [ ] **CA-O22-001:** Una ejecución fresca importa exactamente 100,000 filas y el checkpoint avanza a 100,000.
- [ ] **CA-O22-002:** Ejecutar el importador dos veces seguidas sin modificar el CSV produce el mismo estado final (idempotencia vía `INSERT OR REPLACE`).
- [ ] **CA-O22-003:** Interrumpir el proceso en la fila 250,001 y reanudarlo continúa desde esa fila sin duplicados.

## CU-O23 — Monitorear Drift del Dataset de Vuelos
- [ ] **CA-O23-001:** El cronjob `drift-monitor.yml` ejecuta los lunes a las 06:00 AM UTC.
- [ ] **CA-O23-002:** Con PSI = 0.04 el estado es `stable` y no se envía alerta.
- [ ] **CA-O23-003:** Con PSI = 0.38 el estado es `critical` y se envía alerta a Slack.

## CU-T04 — Monitorear Pipelines ETL y Calidad
- [ ] **CA-T04-001:** La alerta en Slack debe generarse en menos de 1 minuto tras la falla de un nodo del pipeline.
- [ ] **CA-T04-002:** El linaje de los datos debe poder trazarse desde la tabla de destino (PocketBase (Operativa) y MonetDB (Analítica)) hasta la tabla origen (Raw S3) para facilitar el debug.
