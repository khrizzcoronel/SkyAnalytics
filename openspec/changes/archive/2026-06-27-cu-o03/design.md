## Context

Como dictamina el `plan.md` operativo, las cargas de trabajo ETL se deben orquestar en GitHub Actions, pero el código *core* reside en un script agnóstico de Python. Esto garantiza que la carga de un lote CSV crudo pueda validarse, separando las filas malas hacia una capa `Quarantine` y las sanas hacia una capa de `Staging`.

## Goals / Non-Goals

**Goals:**
- Simular la recepción de un CSV grande (Pandas DataFrame).
- Validar las columnas requeridas (por ejemplo, `flight_id`, `status` y `monto_pago`).
- Separar de la carga principal cualquier fila que tenga errores (nulos críticos o mal formados).
- Simular la persistencia masiva en Base de Datos para las filas correctas.

**Non-Goals:**
- No configuraremos Airflow ni GitHub actions `.yaml` en este paso, sino la lógica ETL de Python que será llamada por Actions.
- No instalaremos el conector real ODBC de MonetDB, usaremos un Stub / Mock de volcado (`dump_to_db_stub`).

## Decisions

- **Pandas como motor de procesamiento en memoria:** Para el nivel de carga esperado (lotes diarios de unos pocos Gigabytes), Pandas (o Polars) es suficientemente rápido y consume poca memoria si se procesa en `chunks`.
- **Patrón Fail-Safe de Cuarentena:** Se creará la clase `DataValidator` que iterará o filtrará vectorialmente el DataFrame. Las filas rechazadas se guardarán en `s3://sky-data-raw/quarantine/` (simulado en disco local `tmp/quarantine/`).
- **Idempotencia:** En un entorno real, antes del volcado (Load) a `Staging`, se ejecuta un `DELETE FROM Staging WHERE batch_date = hoy`. Esto garantiza que, si el script falla a la mitad, reejecutarlo no duplique registros.

## Risks / Trade-offs

- **Memoria OOM (Out Of Memory):** Si el CSV supera la memoria RAM de la VPS, Pandas se colgará.
  - *Mitigación:* Se estructurará el script usando `chunksize` al leer el CSV, permitiendo procesar el archivo en bloques de 100k filas secuencialmente.
