## Why
El entrenamiento del modelo XGBoost de predicción de retrasos requiere un dataset de features consolidado. Este dataset debe generarse desde MonetDB (fuente analítica autorizada) y exportarse a S3 para ser consumido por el pipeline de entrenamiento (`CU-O05`).

## What Changes
- Nuevo caso de uso `CU-O24` bajo el módulo `04-ml`.
- Script `backend/src/ml/feature_engineering.py` que:
  - Lee `vw_delay_analysis` desde MonetDB.
  - Calcula features: `airline_delay_avg`, `is_peak_hour`, `is_long_haul`, `is_weekend`.
  - Exporta Parquet local y lo sube a S3 con encriptación AES-256/KMS.

## Capabilities
- `ml-training-pipeline`: Generación de features desde el data warehouse hacia S3.

## Acceptance Criteria
- El pipeline corre domingos a las 05:00 AM (antes de `CU-O05`).
- El Parquet contiene las columnas de features acordadas.
- El upload a S3 usa el bucket configurable `S3_ML_BUCKET`.
