import pandas as pd
import pymonetdb
import boto3

from src.ml import feature_engineering as fe


def test_feature_engineering_creates_columns(monkeypatch, tmp_path):
    df = pd.DataFrame({
        "id": ["fl1", "fl2", "fl3"],
        "year": [2024, 2024, 2024],
        "month": [1, 1, 1],
        "day_of_week": [1, 2, 3],
        "is_weekend": [0, 0, 1],
        "carrier_code": ["AA", "AA", "DL"],
        "distance": [300.0, 500.0, 2000.0],
        "air_time": [60.0, 90.0, 300.0],
        "taxi_out": [10.0, 15.0, 20.0],
        "crs_dep_time": [800.0, 1800.0, 700.0],
        "dep_delay": [5.0, 10.0, 15.0],
    })

    class FakeConn:
        def cursor(self):
            return self
        def close(self):
            pass

    def fake_connect(*args, **kwargs):
        return FakeConn()

    def fake_read_sql(query, conn):
        return df

    class FakeS3:
        def upload_file(self, *args, **kwargs):
            pass

    monkeypatch.setattr(pymonetdb, "connect", fake_connect)
    monkeypatch.setattr(pd, "read_sql_query", fake_read_sql)
    monkeypatch.setattr(boto3, "client", lambda service: FakeS3())
    monkeypatch.setattr(fe, "OUTPUT_DIR", str(tmp_path))

    fe.run_feature_engineering()

    parquet_path = tmp_path / "delay_prediction_2024.parquet"
    assert parquet_path.exists()

    result = pd.read_parquet(parquet_path)
    assert "airline_delay_avg" in result.columns
    assert "is_peak_hour" in result.columns
    assert "is_long_haul" in result.columns
    assert "is_weekend" in result.columns
    assert "dep_delay" in result.columns
