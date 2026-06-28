import pandas as pd
import os

class DataValidator:
    @staticmethod
    def separate_bad_rows(df: pd.DataFrame, quarantine_path: str) -> pd.DataFrame:
        """
        Evalúa las reglas críticas:
        1. flight_id no debe ser nulo o vacío
        2. monto_pago debe ser numérico convertible
        """
        # Guardar copia del tamaño original
        original_size = len(df)
        
        # 1. Encontrar nulls en flight_id
        bad_flight_id = df['flight_id'].isna() | (df['flight_id'] == '')
        
        # 2. Encontrar numéricos corruptos en monto_pago
        # pd.to_numeric con coerce vuelve NaN lo que no es número
        monto_numerico = pd.to_numeric(df['monto_pago'], errors='coerce')
        bad_monto = monto_numerico.isna() & df['monto_pago'].notna()
        
        # Combinar máscaras (OR)
        corrupted_mask = bad_flight_id | bad_monto
        
        corrupted_df = df[corrupted_mask]
        healthy_df = df[~corrupted_mask]
        
        if not corrupted_df.empty:
            # Guardar en cuarentena
            os.makedirs(os.path.dirname(quarantine_path), exist_ok=True)
            # Append por si procesamos en chunks
            corrupted_df.to_csv(quarantine_path, mode='a', header=not os.path.exists(quarantine_path), index=False)
            print(f"[Cuarentena] Se desviaron {len(corrupted_df)} registros defectuosos a {quarantine_path}")
            
        return healthy_df
