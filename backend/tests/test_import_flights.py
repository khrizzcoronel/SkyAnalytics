import importlib
import importlib.util
import os
import sqlite3
import tempfile
from pathlib import Path


def _load_import_module():
    spec = importlib.util.spec_from_file_location(
        "import_flights", Path(__file__).parent.parent / "import" / "import_flights.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _create_flights_raw_table(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE flights_raw (
            id TEXT PRIMARY KEY,
            created TEXT,
            updated TEXT,
            fl_date TEXT,
            op_unique_carrier TEXT,
            op_carrier_fl_num REAL,
            origin TEXT,
            dest TEXT,
            dep_delay REAL,
            arr_delay REAL,
            cancelled INTEGER,
            cancellation_code TEXT,
            diverted INTEGER,
            air_time REAL,
            distance REAL,
            carrier_delay REAL,
            weather_delay REAL,
            nas_delay REAL,
            late_aircraft_delay REAL,
            origin_city_name TEXT,
            origin_state_nm TEXT,
            dest_city_name TEXT,
            dest_state_nm TEXT,
            year REAL,
            month REAL,
            day_of_month REAL,
            day_of_week REAL,
            crs_dep_time REAL,
            dep_time REAL,
            taxi_out REAL,
            wheels_off REAL,
            wheels_on REAL,
            taxi_in REAL,
            crs_arr_time REAL,
            arr_time REAL,
            crs_elapsed_time REAL,
            actual_elapsed_time REAL,
            security_delay REAL
        )
    """)
    conn.commit()
    conn.close()


def test_import_chunk_inserts_rows(monkeypatch, tmp_path):
    csv_path = tmp_path / "flights.csv"
    db_path = tmp_path / "pb_data.db"
    checkpoint_path = tmp_path / "checkpoint.json"

    headers = [
        "year", "month", "day_of_month", "day_of_week", "fl_date",
        "op_unique_carrier", "op_carrier_fl_num", "origin", "origin_city_name",
        "origin_state_nm", "dest", "dest_city_name", "dest_state_nm",
        "crs_dep_time", "dep_time", "dep_delay", "taxi_out", "wheels_off",
        "wheels_on", "taxi_in", "crs_arr_time", "arr_time", "arr_delay",
        "cancelled", "cancellation_code", "diverted", "crs_elapsed_time",
        "actual_elapsed_time", "air_time", "distance", "carrier_delay",
        "weather_delay", "nas_delay", "security_delay", "late_aircraft_delay"
    ]
    rows = [
        "2024,1,1,1,2024-01-01,AA,100,JFK,New York,NY,LAX,Los Angeles,CA,900,915,5,20,30,45,1000,1020,1100,180,3000,10,0,0,0,0,5",
        "2024,1,2,2,2024-01-02,DL,200,ATL,Atlanta,GA,ORD,Chicago,IL,800,810,0,15,25,40,950,1010,1030,150,700,0,0,0,0,0,0",
    ]
    csv_path.write_text(",".join(headers) + "\n" + "\n".join(rows) + "\n")

    _create_flights_raw_table(str(db_path))

    monkeypatch.setenv("CSV_PATH", str(csv_path))
    monkeypatch.setenv("DB_PATH", str(db_path))
    monkeypatch.setenv("CHECKPOINT_FILE", str(checkpoint_path))

    module = _load_import_module()
    module.import_chunk()

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM flights_raw")
    count = cursor.fetchone()[0]
    conn.close()

    assert count == 2
    assert checkpoint_path.exists()
