import sys
import os
import pandas as pd

# Añadimos el directorio de etl al path para poder importar DataValidator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from etl.data_validator import DataValidator
except ImportError:
    # Fallback if running from a different root
    pass

class DataQualityThresholdError(Exception):
    """Excepción lanzada cuando se rompe el Circuit Breaker."""
    pass

class DataQualitySuite:
    def __init__(self, tolerance_rate: float = 0.01):
        self.tolerance_rate = tolerance_rate
        
    def run_suite(self, staging_data: list[dict], quarantine_path: str = "./quarantine_temp.csv"):
        """
        Calcula el ratio de error basándose en DataValidator (el cual implementa las reglas).
        """
        total_records = len(staging_data)
        if total_records == 0:
            return True
            
        df_raw = pd.DataFrame(staging_data)
        
        # Eliminar archivo de cuarentena previo si existe
        if os.path.exists(quarantine_path):
            os.remove(quarantine_path)
            
        # Utilizamos el validador real del ETL
        df_clean = DataValidator.separate_bad_rows(df_raw, quarantine_path)
        
        bad_records = total_records - len(df_clean)
        error_rate = bad_records / total_records
        
        print(f"[DATA QUALITY] Total: {total_records} | Bad: {bad_records} | Error Rate: {error_rate:.2%}")
        
        if error_rate > self.tolerance_rate:
            # Circuit Breaker: Falla duro
            raise DataQualityThresholdError(
                f"Calidad de datos inaceptable. Tasa de error ({error_rate:.2%}) "
                f"supera el límite ({self.tolerance_rate:.2%}). "
                "ABORTO PROMOCIÓN A CORE."
            )
            
        print("[DATA QUALITY] Suite superada. Procediendo a promoción...")
        self.promote_to_core(len(df_clean))
        return True

    def promote_to_core(self, valid_records_count: int):
        """
        Stub que simula la transformación dbt e inserción a fact_flights.
        """
        print(f"[DBT STUB] Promoviendo e insertando {valid_records_count} registros a fact_flights (Core).")
