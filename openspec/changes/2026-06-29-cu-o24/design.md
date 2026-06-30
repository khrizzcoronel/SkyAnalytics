## Context
`vw_delay_analysis` ya contiene los datos limpios del Star Schema. A partir de ahí se agregan features matemáticas que mejoran la predicción de retrasos.

## Decisions
- **Features calculadas:**
  - `airline_delay_avg`: retraso promedio histórico por aerolínea.
  - `is_peak_hour`: 1 si hora de salida está en 07-09 o 17-19.
  - `is_long_haul`: 1 si `distance > 1500` millas.
  - `is_weekend`: ya presente en `vw_delay_analysis`.
- **Target variable:** `dep_delay`.
- **Salida:** Parquet local + upload a S3 con `ServerSideEncryption=AES256`.
- **Bucket configurable:** `S3_ML_BUCKET` desde env (default staging-friendly).

## Files Changed
- `backend/src/ml/feature_engineering.py`
- `specs/003-operativo/CU-O24.md` (a completar en Fase 2)

## Dependencies
- MonetDB con `vw_delay_analysis` poblada por `CU-O21`.
- Credenciales AWS con permisos de escritura al bucket S3.
