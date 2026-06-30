# Especificación de Caso de Uso: CU-O24

## 1. Nombre de la Funcionalidad
**Generar Features para Modelo ML desde MonetDB**

## 2. Objetivo
Construir y persistir el dataset de características técnicas (features) optimizadas y necesarias para entrenar el modelo predictivo de retrasos de vuelos (XGBoost), extrayendo la información consolidada desde el Data Warehouse analítico de MonetDB y exportándola en formato Parquet a S3.

## 3. Actores Involucrados
- **Actor Principal:** GitHub Actions (Cron) / Sistema
- **Sistemas Secundarios:** MonetDB, AWS S3

## 4. Contexto del Problema
Entrenar un modelo de Machine Learning directamente desde los datos operativos crudos genera bajo rendimiento debido a la falta de variables agregadas históricas. Este proceso realiza la agregación matemática en caliente en MonetDB y consolida el dataset listo para el consumo del algoritmo.

## 5. Requisitos Funcionales
- **RF-O24-001:** El pipeline debe ejecutarse de forma programada antes del reentrenamiento del modelo (ej. domingos a las 05:00 AM).
- **RF-O24-002:** Debe calcular variables a nivel de aerolínea y ruta (ej. `airline_delay_avg`).
- **RF-O24-003:** Debe procesar métricas de tiempo (`is_weekend`, `is_peak_hour`).
- **RF-O24-004:** Debe guardar el resultado en un archivo Parquet local.
- **RF-O24-005:** Debe subir el archivo a S3 bajo un esquema encriptado KMS.

## 6. Requisitos No Funcionales
- **RNF-O24-001 (Performance):** La extracción y transformación de las features debe ejecutarse en menos de 10 minutos.

## 7. Escenarios (Gherkin)

### Escenario 1: Generación exitosa de features
- **DADO** que MonetDB tiene las tablas analíticas actualizadas
- **CUANDO** el pipeline de Feature Engineering se dispara
- **ENTONCES** calcula las métricas agregadas por ruta y aerolínea
- **Y** exporta el dataset a `s3://skyanalytics-ml/features/delay_prediction_2024.parquet`.

## 8. Reglas de Negocio
- **RN-O24-001 (Features estándar):** El dataset debe incl obligatoriamente `airline_delay_avg`, `is_peak_hour`, `is_long_haul`, `is_weekend` además del target `dep_delay`.
- **RN-O24-002 (Bucket configurable):** El bucket S3 destino se define por la variable de entorno `S3_ML_BUCKET` (default `skyanalytics-ml`).
- **RN-O24-003 (Encriptación):** El objeto Parquet en S3 debe usar encriptación AES-256 (SSE-S3 o KMS).

## 9. Entradas
| Campo | Tipo | Descripción |
|---|---|---|
| `vw_delay_analysis` | Vista MonetDB | Vista plana con retrasos, distancias, tiempos y códigos de aerolínea. |
| `S3_ML_BUCKET` | Env var | Bucket S3 destino. |
| AWS credentials | Env / IAM | Permisos de escritura al bucket. |

## 10. Salidas
| Campo / Objeto | Tipo | Descripción |
|---|---|---|
| `delay_prediction_2024.parquet` | Archivo local | Dataset de features en `./features/`. |
| `s3://<bucket>/features/delay_prediction_2024.parquet` | Objeto S3 | Dataset de features en S3 encriptado. |

## 11. Criterios de Aceptación
- **CA-O24-001:** El Parquet contiene las columnas requeridas: `airline_delay_avg`, `is_peak_hour`, `is_long_haul`, `is_weekend`, `dep_delay`.
- **CA-O24-002:** El archivo se sube correctamente a S3 con encriptación activada.
- **CA-O24-003:** El pipeline finaliza en menos de 10 minutos para 7M filas.

## 12. Restricciones
- Requiere `vw_delay_analysis` poblada (`CU-O21`).
- Requiere credenciales AWS válidas con permisos de escritura al bucket.
- El bucket debe existir previamente.

## 13. Fuera de Alcance
- Entrenamiento del modelo XGBoost (`CU-O05`).
- Champion/Challenger evaluation (`CU-O05`).
- Validación de calidad de features (asumida por `CU-O04`).

## 14. Aclaraciones Globales (Speckit-Clarify)
- **Secretos:** Las credenciales AWS se inyectan vía variables de entorno/GitHub Secrets; no se almacenan en código.

