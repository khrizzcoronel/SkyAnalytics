import os
import pandas as pd
from data_validator import DataValidator

class StagingDatabaseStub:
    def __init__(self):
        self.rows_inserted = 0
        
    def delete_batch(self, date_str: str):
        # Idempotencia: Limpiar lote previo
        print(f"[DB_STUB] DELETE FROM stg_oag_flights WHERE departure_date = '{date_str}'")
        self.rows_inserted = 0

    def insert_many(self, df: pd.DataFrame):
        # Simulamos COPY INTO masivo
        self.rows_inserted += len(df)
        print(f"[DB_STUB] INSERTADOS {len(df)} registros exitosamente.")

def run_etl(source_csv: str, quarantine_csv: str):
    print("--- INICIANDO INGESTA NOCTURNA ---")
    
    db = StagingDatabaseStub()
    
    # 1. Idempotencia: Limpieza (Asumiendo que procesamos lote del dia de hoy)
    # En la vida real, sacaríamos la fecha del nombre del archivo o los metadatos
    db.delete_batch("2026-11-XX")
    
    # Si existe el archivo de cuarentena de corridas previas, lo borramos para esta demo
    if os.path.exists(quarantine_csv):
        os.remove(quarantine_csv)

    chunk_size = 1000 # Chunks pequeños para la demo
    total_processed = 0
    total_healthy = 0
    
    print(f"Leyendo archivo: {source_csv} en chunks de {chunk_size}...")
    
    # 2. Lectura y Procesamiento
    for chunk_idx, chunk in enumerate(pd.read_csv(source_csv, chunksize=chunk_size)):
        print(f"\nProcesando Chunk {chunk_idx + 1}...")
        
        # Validar y separar cuarentena
        healthy_chunk = DataValidator.separate_bad_rows(chunk, quarantine_csv)
        
        # Cargar sanos a DB
        if not healthy_chunk.empty:
            db.insert_many(healthy_chunk)
            
        total_processed += len(chunk)
        total_healthy += len(healthy_chunk)
        
    print("\n--- RESUMEN DE INGESTA ---")
    print(f"Filas procesadas origen : {total_processed}")
    print(f"Filas limpias en Staging: {total_healthy}")
    print(f"Filas en Cuarentena     : {total_processed - total_healthy}")
    print(f"Validación Staging DB   : {db.rows_inserted} registros en total.")

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    source_file = os.path.join(current_dir, 'daily_flights.csv')
    quarantine_file = os.path.join(current_dir, 'quarantine', 'bad_rows.csv')
    
    if not os.path.exists(source_file):
        print(f"Error: No se encontró {source_file}. Ejecuta generate_mock_csv.py primero.")
    else:
        run_etl(source_file, quarantine_file)
