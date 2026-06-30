import pandas as pd
import os
from typing import Tuple

class DataValidator:
    RULES = {
        'missing_carrier': "op_carrier_fl_num nulo",
        'missing_date': "fl_date nulo o vacío",
        'bad_delay': "dep_delay fuera de rango [-120, 1440]",
        'bad_distance': "distance <= 0",
    }

    @staticmethod
    def _build_reasons(df: pd.DataFrame) -> pd.Series:
        """Devuelve una Serie con la(s) razón(es) de cuarentena por fila."""
        reasons = []
        for _, row in df.iterrows():
            r = []
            if pd.isna(row.get('op_carrier_fl_num')):
                r.append(DataValidator.RULES['missing_carrier'])
            if pd.isna(row.get('fl_date')) or row.get('fl_date') == '':
                r.append(DataValidator.RULES['missing_date'])
            delay = row.get('dep_delay')
            if pd.notna(delay) and (delay < -120 or delay > 1440):
                r.append(DataValidator.RULES['bad_delay'])
            distance = row.get('distance')
            if pd.notna(distance) and distance <= 0:
                r.append(DataValidator.RULES['bad_distance'])
            reasons.append(' | '.join(r) if r else '')
        return pd.Series(reasons, index=df.index)

    @staticmethod
    def validate_batch(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
        """
        Evalúa las reglas críticas del dataset BTS.
        Retorna (healthy_df, corrupted_df, reasons_series).
        """
        # 1. Encontrar nulls en columnas críticas
        bad_carrier = df['op_carrier_fl_num'].isna()
        bad_date = df['fl_date'].isna() | (df['fl_date'] == '')

        # 2. Encontrar valores anómalos o fuera de rango lógico
        bad_delay = df['dep_delay'].notna() & ((df['dep_delay'] < -120) | (df['dep_delay'] > 1440))
        bad_distance = df['distance'].notna() & (df['distance'] <= 0)

        # Combinar máscaras (OR)
        corrupted_mask = bad_carrier | bad_date | bad_delay | bad_distance

        corrupted_df = df[corrupted_mask].copy()
        healthy_df = df[~corrupted_mask].copy()

        reasons = DataValidator._build_reasons(corrupted_df)
        corrupted_df['quarantine_reason'] = reasons

        if not corrupted_df.empty:
            print(f"[Cuarentena] Se detectaron {len(corrupted_df)} registros defectuosos")

        return healthy_df, corrupted_df, reasons

    @staticmethod
    def separate_bad_rows(df: pd.DataFrame, quarantine_path: str) -> pd.DataFrame:
        """
        Legacy entrypoint: mantiene compatibilidad con scripts/tests antiguos.
        Escribe registros corruptos a un CSV local.
        """
        healthy_df, corrupted_df, _ = DataValidator.validate_batch(df)

        if not corrupted_df.empty:
            qdir = os.path.dirname(quarantine_path)
            if qdir:
                os.makedirs(qdir, exist_ok=True)
            corrupted_df.to_csv(quarantine_path, mode='a', header=not os.path.exists(quarantine_path), index=False)
            print(f"[Cuarentena CSV] Se desviaron {len(corrupted_df)} registros defectuosos a {quarantine_path}")

        return healthy_df
