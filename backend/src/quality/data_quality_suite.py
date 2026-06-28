import pandas as pd
from pydantic import ValidationError
from contracts import FlightRecordContract

class DataQualityThresholdError(Exception):
    """Excepción lanzada cuando se rompe el Circuit Breaker."""
    pass

class DataQualitySuite:
    def __init__(self, tolerance_rate: float = 0.01):
        self.tolerance_rate = tolerance_rate
        
    def run_suite(self, staging_data: list[dict]):
        """
        Itera la data de Staging (simulada como lista de dicts).
        Calcula el ratio de error basandose en el Contrato Pydantic.
        """
        total_records = len(staging_data)
        if total_records == 0:
            return True
            
        bad_records = 0
        
        for row in staging_data:
            try:
                # Validar cada fila contra el contrato
                FlightRecordContract(**row)
            except ValidationError:
                bad_records += 1
                
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
        self.promote_to_core(total_records - bad_records)
        return True

    def promote_to_core(self, valid_records_count: int):
        """
        Stub que simula la transformación dbt e inserción a Fact_Flight.
        """
        print(f"[DBT STUB] Promoviendo e insertando {valid_records_count} registros a Fact_Flight (Core).")
