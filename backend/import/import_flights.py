import os
import csv
import json
import sqlite3
from datetime import datetime
from datetime import datetime

# Configuración
DB_PATH = os.getenv("DB_PATH", "/pb_data/data.db")
CSV_PATH = os.getenv("CSV_PATH", "/data/flight_data_2024.csv")
CHECKPOINT_FILE = os.getenv("CHECKPOINT_FILE", "/data/importer_checkpoint.json")
CHUNK_SIZE = 100_000
BATCH_SIZE = 10_000  # Tamaño del lote para inserción en SQLite

# Columnas esperadas en el CSV (minúsculas)
CSV_HEADERS = [
    "year", "month", "day_of_month", "day_of_week", "fl_date",
    "op_unique_carrier", "op_carrier_fl_num", "origin", "origin_city_name",
    "origin_state_nm", "dest", "dest_city_name", "dest_state_nm",
    "crs_dep_time", "dep_time", "dep_delay", "taxi_out", "wheels_off",
    "wheels_on", "taxi_in", "crs_arr_time", "arr_time", "arr_delay",
    "cancelled", "cancellation_code", "diverted", "crs_elapsed_time",
    "actual_elapsed_time", "air_time", "distance", "carrier_delay",
    "weather_delay", "nas_delay", "security_delay", "late_aircraft_delay"
]

def generate_deterministic_id(index):
    # Genera un ID de 15 caracteres determinista: 'fl' + index con ceros a la izquierda
    # Ejemplo: fl0000000000001
    return f"fl{str(index).zfill(13)}"

def get_last_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        try:
            with open(CHECKPOINT_FILE, 'r') as f:
                data = json.load(f)
                return data.get("last_row", 0)
        except Exception as e:
            print(f"Error al leer checkpoint, iniciando desde 0: {e}")
    return 0

def save_checkpoint(row_index):
    try:
        checkpoint_dir = os.path.dirname(CHECKPOINT_FILE)
        if checkpoint_dir:
            os.makedirs(checkpoint_dir, exist_ok=True)
        with open(CHECKPOINT_FILE, 'w') as f:
            json.dump({"last_row": row_index, "updated_at": datetime.utcnow().isoformat()}, f)
        print(f"[CHECKPOINT] Guardado en fila {row_index}")
    except Exception as e:
        print(f"Error al guardar checkpoint: {e}")

def import_chunk():
    start_row = get_last_checkpoint()
    print(f"Iniciando importación desde la fila {start_row}...")

    if not os.path.exists(CSV_PATH):
        print(f"Error: No se encontró el dataset en {CSV_PATH}")
        return

    if not os.path.exists(DB_PATH):
        print(f"Error: La base de datos de PocketBase no existe en {DB_PATH}. ¿Inició PocketBase primero?")
        return

    # Conectar a la base de datos SQLite directamente
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Verificar si la tabla flights_raw existe en la DB sqlite de pocketbase
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='flights_raw';")
    if not cursor.fetchone():
        print("La tabla 'flights_raw' no existe en PocketBase todavía. Por favor importa el esquema pb_schema.json primero.")
        conn.close()
        return

    # Leer el CSV
    with open(CSV_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        # Mapear nombres de columnas a índices
        header_map = {col.lower().strip(): idx for idx, col in enumerate(header)}
        
        # Saltar las filas ya procesadas
        for _ in range(start_row):
            try:
                next(reader)
            except StopIteration:
                print("Se alcanzó el fin del archivo CSV.")
                save_checkpoint(start_row)
                conn.close()
                return

        rows_to_insert = []
        current_row = start_row
        processed_in_chunk = 0

        # Preparar query SQL de inserción
        # Columnas reales en la tabla sqlite de PocketBase para flights_raw
        fields = [
            "id", "created", "updated", "fl_date", "op_unique_carrier",
            "op_carrier_fl_num", "origin", "dest", "dep_delay", "arr_delay",
            "cancelled", "cancellation_code", "diverted", "air_time", "distance",
            "carrier_delay", "weather_delay", "nas_delay", "late_aircraft_delay",
            "origin_city_name", "origin_state_nm", "dest_city_name", "dest_state_nm",
            # Guardamos campos extras solicitados por el usuario
            "year", "month", "day_of_month", "day_of_week", "crs_dep_time",
            "dep_time", "taxi_out", "wheels_off", "wheels_on", "taxi_in",
            "crs_arr_time", "arr_time", "crs_elapsed_time", "actual_elapsed_time",
            "security_delay"
        ]

        query = f"INSERT OR REPLACE INTO flights_raw ({', '.join(fields)}) VALUES ({', '.join(['?'] * len(fields))})"

        now_iso = datetime.utcnow().isoformat().replace('T', ' ') + 'Z'

        for row in reader:
            current_row += 1
            processed_in_chunk += 1
            
            # Helper para extraer valor
            def val(col_name, default=None, is_num=False, is_bool=False):
                idx = header_map.get(col_name)
                if idx is None or idx >= len(row):
                    return default
                raw_val = row[idx].strip()
                if raw_val == "":
                    return default
                if is_bool:
                    return 1 if raw_val in ("1", "1.0", "True", "true") else 0
                if is_num:
                    try:
                        return float(raw_val) if "." in raw_val else int(float(raw_val))
                    except ValueError:
                        return default
                return raw_val

            # Mapear
            record_id = generate_deterministic_id(current_row)
            
            record_data = (
                record_id,
                now_iso,
                now_iso,
                val("fl_date"),
                val("op_unique_carrier"),
                val("op_carrier_fl_num", is_num=True),
                val("origin"),
                val("dest"),
                val("dep_delay", is_num=True),
                val("arr_delay", is_num=True),
                val("cancelled", is_bool=True),
                val("cancellation_code"),
                val("diverted", is_bool=True),
                val("air_time", is_num=True),
                val("distance", is_num=True),
                val("carrier_delay", is_num=True),
                val("weather_delay", is_num=True),
                val("nas_delay", is_num=True),
                val("late_aircraft_delay", is_num=True),
                val("origin_city_name"),
                val("origin_state_nm"),
                val("dest_city_name"),
                val("dest_state_nm"),
                # Extras
                val("year", is_num=True),
                val("month", is_num=True),
                val("day_of_month", is_num=True),
                val("day_of_week", is_num=True),
                val("crs_dep_time", is_num=True),
                val("dep_time", is_num=True),
                val("taxi_out", is_num=True),
                val("wheels_off", is_num=True),
                val("wheels_on", is_num=True),
                val("taxi_in", is_num=True),
                val("crs_arr_time", is_num=True),
                val("arr_time", is_num=True),
                val("crs_elapsed_time", is_num=True),
                val("actual_elapsed_time", is_num=True),
                val("security_delay", is_num=True)
            )

            rows_to_insert.append(record_data)

            # Inserción por lotes para optimizar transacciones de SQLite
            if len(rows_to_insert) >= BATCH_SIZE:
                cursor.executemany(query, rows_to_insert)
                conn.commit()
                rows_to_insert = []
                print(f"Insertados {current_row} registros en total...")

            if processed_in_chunk >= CHUNK_SIZE:
                break

        # Insertar los registros restantes
        if rows_to_insert:
            cursor.executemany(query, rows_to_insert)
            conn.commit()
            print(f"Insertados {current_row} registros en total...")

        conn.close()
        save_checkpoint(current_row)
        print(f"Fin del lote. Se procesaron {processed_in_chunk} registros en esta corrida. Checkpoint: {current_row}")

if __name__ == "__main__":
    import_chunk()
