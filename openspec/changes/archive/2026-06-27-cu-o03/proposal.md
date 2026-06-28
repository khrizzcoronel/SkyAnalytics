## Why

Los dashboards estratégicos necesitan datos frescos. Las fuentes de datos (ej. OAG, NOAA) envían periódicamente archivos masivos CSV que deben procesarse. Sin un proceso ETL robusto que cuente con mecanismos de cuarentena y limpieza inicial, un solo dato corrupto en un archivo de gigabytes causaría un fallo catastrófico en todo el sistema analítico.

## What Changes

- **Flujo de Ingesta ETL**: Script de Python que simula la extracción de un archivo masivo CSV desde un SFTP.
- **Cuarentena de Datos**: Implementación de lógica `DataValidator` en Python para desviar filas malas (ej. sin fecha o nulas) hacia un "Quarantine Store".
- **Carga en Staging**: Volcado masivo (simulado) hacia la tabla `Fact_Flight` (Staging) utilizando Pandas u operaciones masivas seguras, garantizando idempotencia.

## Capabilities

### New Capabilities
- `etl-ingestion-pipeline`: Orquestador principal de la carga (Extract, Normalize, Load).
- `data-quarantine-guard`: Componente validador que aparta datos corruptos sin detener el lote principal.

### Modified Capabilities
- 

## Impact

- **Backend (Python)**: Nuevo script en `backend/src/etl/ingestion_job.py`.
- **Librerías**: Adición de `pandas` para el procesamiento rápido de grandes volúmenes de datos tabulares.
- **Resiliencia**: El sistema tolerará fallos parciales de datos (Soft Errors) gracias al sistema de cuarentena.
