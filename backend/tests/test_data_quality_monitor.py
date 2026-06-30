from src.tactical.data_quality_monitor import DataQualityMonitor


def test_validate_schema_accepts_clean_data():
    monitor = DataQualityMonitor()
    data = [
        {"flight_id": "DL123", "departure": "2026-07-01T10:00"},
        {"flight_id": "UA456", "departure": "2026-07-01T12:00"},
    ]
    assert monitor.validate_schema(data) is True


def test_validate_schema_rejects_null_flight_id():
    monitor = DataQualityMonitor()
    data = [
        {"flight_id": "AA789", "departure": "2026-07-01T15:00"},
        {"flight_id": None, "departure": "2026-07-01T18:00"},
    ]
    assert monitor.validate_schema(data) is False
