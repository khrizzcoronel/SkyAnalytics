import os
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import boto3

S3_ML_BUCKET = os.getenv("S3_ML_BUCKET", "skyanalytics-ml")
ML_FALLBACK_MOCK = os.getenv("ML_FALLBACK_MOCK", "true").lower() in ("1", "true", "yes")


def download_data_from_s3(bucket_name, file_key, download_path):
    print(f"[AWS S3] Descargando features desde s3://{bucket_name}/{file_key}...")
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, file_key, download_path)
        print("[AWS S3] Descarga exitosa.")
        return True
    except Exception as e:
        print(f"[AWS S3] Fallo en la descarga: {e}")
        return False

def train_xgboost():
    print("Iniciando Pipeline de Entrenamiento XGBoost...")
    
    # 1. Carga de Datos
    local_data_path = "./features_temp.parquet"
    if not download_data_from_s3(S3_ML_BUCKET, 'features/delay_prediction_2024.parquet', local_data_path):
        if not ML_FALLBACK_MOCK:
            print("ERROR: No se pudo descargar features desde S3 y ML_FALLBACK_MOCK=false")
            return
        print("Intentando cargar datos de pruebas localmente si existen...")
        # Generar data dummy si no hay internet o s3 falla, para que el script no explote en desarrollo
        np.random.seed(42)
        X_dummy = pd.DataFrame(np.random.rand(1000, 10), columns=[f'feature_{i}' for i in range(10)])
        y_dummy = pd.Series(np.random.rand(1000) * 100)
        df = pd.concat([X_dummy, y_dummy.rename('target')], axis=1)
    else:
        try:
            df = pd.read_parquet(local_data_path)
        except Exception as e:
            print(f"Error leyendo parquet: {e}")
            return
            
    # Asumimos que la columna objetivo se llama 'dep_delay' o 'target'
    target_col = 'dep_delay' if 'dep_delay' in df.columns else 'target'
    
    if target_col not in df.columns:
        print(f"Columna objetivo {target_col} no encontrada. Abortando.")
        return
        
    X = df.drop(columns=[target_col, 'id', 'pb_created', 'fl_date'], errors='ignore')
    y = df[target_col]
    
    # Manejar nulos
    X = X.fillna(0)
    y = y.fillna(0)
    
    # One-Hot Encoding para categóricas
    X = pd.get_dummies(X)
    
    print(f"Dataset cargado. Forma: {X.shape}")
    
    # 2. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Entrenamiento XGBoost
    print("Entrenando modelo XGBoost...")
    model = xgb.XGBRegressor(
        objective='reg:squarederror',
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # 4. Evaluación
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Calculo seguro de MAPE evitando division por 0
    mape = np.mean(np.abs((y_test - y_pred) / np.where(y_test == 0, 1e-8, y_test))) * 100
    
    print("-" * 30)
    print("MÉTRICAS DEL MODELO XGBOOST")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE : {mae:.4f}")
    print(f"R²  : {r2:.4f}")
    print(f"MAPE: {mape:.2f}%")
    print("-" * 30)
    
    # 5. Guardar el Modelo
    model_filename = 'xgboost_delay_model.pkl'
    joblib.dump(model, model_filename)
    print(f"Modelo guardado exitosamente como {model_filename}")
    
    # Subir modelo a S3
    print(f"[AWS S3] Subiendo {model_filename} a s3://{S3_ML_BUCKET}/models/...")
    try:
        s3 = boto3.client('s3')
        s3.upload_file(model_filename, S3_ML_BUCKET, f'models/{model_filename}')
        print("[AWS S3] Upload exitoso.")
    except Exception as e:
        print(f"[AWS S3] Omitiendo upload de modelo (Falta de credenciales): {e}")

if __name__ == "__main__":
    train_xgboost()
