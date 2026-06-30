import pandas as pd
from src.etl.data_validator import DataValidator


def test_validate_batch_accepts_clean_rows():
    df = pd.DataFrame({
        "id": ["fl1"],
        "fl_date": ["2024-01-01"],
        "op_carrier_fl_num": [1234],
        "dep_delay": [10.0],
        "distance": [500.0],
    })
    healthy, corrupted, _ = DataValidator.validate_batch(df)
    assert len(healthy) == 1
    assert len(corrupted) == 0


def test_validate_batch_quarantines_bad_rows():
    df = pd.DataFrame({
        "id": ["fl1", "fl2", "fl3", "fl4"],
        "fl_date": ["2024-01-01", None, "2024-01-03", "2024-01-04"],
        "op_carrier_fl_num": [1234, 5678, None, 9999],
        "dep_delay": [10.0, 2000.0, 5.0, -200.0],
        "distance": [500.0, 100.0, -10.0, 300.0],
    })
    healthy, corrupted, reasons = DataValidator.validate_batch(df)
    assert len(healthy) == 1
    assert len(corrupted) == 3
    # fl3 tiene distance <= 0
    assert "distance <= 0" in corrupted.iloc[1]["quarantine_reason"]
