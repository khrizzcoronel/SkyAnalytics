## ADDED Requirements

### Requirement: Feature Engineering Pipeline from MonetDB
El sistema SHALL generar un dataset de features para entrenamiento XGBoost a partir de `vw_delay_analysis` en MonetDB y exportarlo como Parquet encriptado a S3.

#### Scenario: Generación semanal de features
- **WHEN** el pipeline `feature_engineering.py` ejecuta los domingos a las 05:00 AM
- **THEN** lee `vw_delay_analysis` desde MonetDB
- **AND** calcula `airline_delay_avg`, `is_peak_hour`, `is_long_haul`, `is_weekend`
- **AND` escribe `delay_prediction_2024.parquet` localmente
- **AND** sube el archivo a `s3://<S3_ML_BUCKET>/features/` con encriptación AES-256/KMS.

### Requirement: S3 ML Bucket Configuration
El pipeline SHALL usar el bucket definido por la variable de entorno `S3_ML_BUCKET` en lugar de un nombre hardcoded.

#### Scenario: Bucket configurable
- **WHEN** `S3_ML_BUCKET=skyanalytics-ml-staging`
- **THEN** el upload de features usa ese bucket sin modificar código.
