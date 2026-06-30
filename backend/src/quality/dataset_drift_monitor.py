import os
import pandas as pd
import numpy as np
import pymonetdb

MONETDB_HOST = os.getenv("MONETDB_HOST", "monetdb")
MONETDB_PORT = int(os.getenv("MONETDB_PORT", 50000))
MONETDB_USER = os.getenv("MONETDB_USER", "monetdb")
MONETDB_PASS = os.getenv("MONETDB_PASS")
MONETDB_DB = os.getenv("MONETDB_DB", "demo")

def calculate_psi(expected, actual, num_buckets=10):
    """
    Calcula de forma simplificada el Population Stability Index (PSI).
    """
    expected = expected + 1e-5
    actual = actual + 1e-5
    
    percentiles = np.linspace(0, 100, num_buckets + 1)
    buckets = np.percentile(expected, percentiles)
    
    expected_counts, _ = np.histogram(expected, bins=buckets)
    actual_counts, _ = np.histogram(actual, bins=buckets)
    
    expected_pct = expected_counts / len(expected)
    actual_pct = actual_counts / len(actual)
    
    psi_value = 0.0
    for e_pct, a_pct in zip(expected_pct, actual_pct):
        if e_pct > 0 and a_pct > 0:
            psi_value += (a_pct - e_pct) * np.log(a_pct / e_pct)
            
    return psi_value

def run_drift_monitor():
    if not MONETDB_PASS:
        raise ValueError("MONETDB_PASS environment variable is required")

    print("--- INICIANDO MONITOREO DE DATASET DRIFT REAL (CU-O23) ---")
    
    print("Conectando a MonetDB para obtener datos de retrasos...")
    try:
        conn = pymonetdb.connect(
            host=MONETDB_HOST, port=MONETDB_PORT,
            username=MONETDB_USER, password=MONETDB_PASS, database=MONETDB_DB
        )
        
        # Extraemos retrasos ordenados por fecha
        query = "SELECT fl_date, dep_delay FROM vw_delay_analysis ORDER BY fl_date"
        df = pd.read_sql_query(query, conn)
        conn.close()
    except Exception as e:
        print(f"Error al conectar a MonetDB: {e}")
        return
        
    if df.empty or len(df) < 100:
        print("No hay suficientes datos en MonetDB para calcular drift (mínimo 100 registros).")
        return
        
    # Asumimos que el 80% más antiguo es el histórico (entrenamiento) y el 20% más reciente es la nueva distribución
    split_idx = int(len(df) * 0.8)
    historical_delays = df['dep_delay'].iloc[:split_idx].values
    new_delays = df['dep_delay'].iloc[split_idx:].values
    
    print(f"Datos Históricos (Baseline): {len(historical_delays)} registros")
    print(f"Datos Recientes (Challenger): {len(new_delays)} registros")

    print("\n--- Analizando Drift ---")
    psi = calculate_psi(historical_delays, new_delays)
    print(f"PSI Calculado: {psi:.4f}")
    if psi > 0.25:
        print("[ALERTA] [ROJO] ¡Alerta de Drift en retrasos! El perfil estadístico ha cambiado de forma severa.")
        print("[SLACK NOTIFICATION] Enviando aviso a #data-ops: Posible degradación del modelo XGBoost debido a anomalías en retrasos.")
    elif psi > 0.1:
        print("[AVISO] [AMARILLO] Drift moderado detectado. Vigilar rendimiento del modelo.")
    else:
        print("[VERDE] Perfil de datos estable. No se requiere acción.")

    print("\n--- MONITOREO DE DRIFT FINALIZADO ---")

if __name__ == "__main__":
    run_drift_monitor()
