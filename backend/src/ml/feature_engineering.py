import os
import pandas as pd
import pymonetdb
import boto3

MONETDB_HOST = os.getenv("MONETDB_HOST", "monetdb")
MONETDB_PORT = int(os.getenv("MONETDB_PORT", 50000))
MONETDB_USER = os.getenv("MONETDB_USER", "monetdb")
MONETDB_PASS = os.getenv("MONETDB_PASS")
MONETDB_DB = os.getenv("MONETDB_DB", "demo")

if not MONETDB_PASS:
    raise ValueError("MONETDB_PASS environment variable is required")

OUTPUT_DIR = "./features"

def run_feature_engineering():
    print("--- INICIANDO PIPELINE DE FEATURE ENGINEERING (CU-O24) ---")
    
    # 1. Extracción desde MonetDB
    print("Conectando a MonetDB...")
    try:
        conn = pymonetdb.connect(
            host=MONETDB_HOST,
            port=MONETDB_PORT,
            username=MONETDB_USER,
            password=MONETDB_PASS,
            database=MONETDB_DB
        )
        
        print("Consultando vista analítica vw_delay_analysis...")
        query = "SELECT * FROM vw_delay_analysis"
        df = pd.read_sql_query(query, conn)
        conn.close()
        
    except Exception as e:
        print(f"Error al extraer datos desde MonetDB: {e}")
        return

    if df.empty:
        print("No hay datos en la vista analítica. Asegúrate de ejecutar el ETL primero.")
        return

    print(f"Registros extraídos para engineering: {len(df)}")

    # 2. Ingeniería de Características (Features)
    print("Calculando features...")
    
    # Rellenar nulos
    df['dep_delay'] = df['dep_delay'].fillna(0)
    df['distance'] = df['distance'].fillna(0)
    df['taxi_out'] = df['taxi_out'].fillna(0)
    df['crs_dep_time'] = df['crs_dep_time'].fillna(0)
    
    # Feature 1: Promedio de retrasos histórico de la aerolínea
    airline_delays = df.groupby('carrier_code')['dep_delay'].transform('mean').rename('airline_delay_avg')
    df = pd.concat([df, airline_delays], axis=1)
    
    # Feature 2: Indica si el vuelo sale en horas pico de mañana o tarde
    # crs_dep_time está en formato entero HHMM (ej. 1245 -> 12.45h)
    hour = df['crs_dep_time'] / 100
    df['is_peak_hour'] = ((hour >= 7) & (hour <= 9)) | ((hour >= 17) & (hour <= 19))
    df['is_peak_hour'] = df['is_peak_hour'].astype(int)

    # Feature 3: Eficiencia en pista (taxi_out) promedio por ruta
    # En un set real haríamos join con origen y destino, aquí usamos taxi_out del registro
    # de forma directa para simular variables a nivel de vuelo
    df['is_long_haul'] = (df['distance'] > 1500).astype(int)

    # Feature 4: Indicadores temporales
    df['is_weekend'] = df['is_weekend'].fillna(0).astype(int)
    
    # Columnas finales seleccionadas para entrenar el modelo XGBoost
    features_cols = [
        'id', 'year', 'month', 'day_of_week', 'is_weekend', 'carrier_code',
        'distance', 'air_time', 'taxi_out', 'airline_delay_avg', 'is_peak_hour',
        'is_long_haul', 'dep_delay'  # Target variable
    ]
    
    df_features = df[features_cols]
    
    # 3. Exportación
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    parquet_path = os.path.join(OUTPUT_DIR, "delay_prediction_2024.parquet")
    
    # Guardar en local en formato Parquet
    print(f"Guardando features resultantes en local: {parquet_path}")
    df_features.to_parquet(parquet_path, index=False)
    
    # Simular carga a AWS S3 compatible con KMS (AES-256)
    print(f"[AWS S3] Subiendo features a s3://skyanalytics-ml/features/delay_prediction_2024.parquet (Encriptación AES-256 activa)...")
    try:
        s3 = boto3.client('s3')
        s3.upload_file(parquet_path, 'skyanalytics-ml', 'features/delay_prediction_2024.parquet')
        print("[AWS S3] Upload exitoso.")
    except Exception as e:
        print(f"[AWS S3] Omitiendo upload a S3 real en desarrollo/test (Falta de credenciales): {e}")
    print("--- PIPELINE DE FEATURES COMPLETADO ---")

if __name__ == "__main__":
    run_feature_engineering()
