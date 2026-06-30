import sys
import os
import sqlite3
import pandas as pd
import pymonetdb

sys.path.insert(0, os.path.dirname(__file__))
from data_validator import DataValidator

# Configuración de entornos
PB_DB_PATH = os.getenv("PB_DB_PATH", "/pb_data/data.db")
MONETDB_HOST = os.getenv("MONETDB_HOST", "monetdb")
MONETDB_PORT = int(os.getenv("MONETDB_PORT", 50000))
MONETDB_USER = os.getenv("MONETDB_USER", "monetdb")
MONETDB_PASS = os.getenv("MONETDB_PASS")
MONETDB_DB = os.getenv("MONETDB_DB", "demo")

if not MONETDB_PASS:
    raise ValueError("MONETDB_PASS environment variable is required")

def run_etl():
    print("--- INICIANDO ETL: POCKETBASE -> MONETDB (STAR SCHEMA) ---")
    
    if not os.path.exists(PB_DB_PATH):
        print(f"Error: No se encontró la base de datos de PocketBase en {PB_DB_PATH}")
        return

    # 0. Obtener estado previo de MonetDB para Incremental Load
    print("Conectando a MonetDB para estado previo...")
    last_created = None
    try:
        m_conn_meta = pymonetdb.connect(
            host=MONETDB_HOST, port=MONETDB_PORT,
            username=MONETDB_USER, password=MONETDB_PASS, database=MONETDB_DB
        )
        cursor_meta = m_conn_meta.cursor()
        
        # Tablas pueden no existir en primera corrida
        try:
            # Intentar parchear la tabla si viene de versión anterior
            try:
                cursor_meta.execute("ALTER TABLE fact_flights ADD COLUMN pb_created TIMESTAMP;")
                m_conn_meta.commit()
            except Exception:
                pass # Ya existe
                
            cursor_meta.execute("SELECT MAX(pb_created) FROM fact_flights")
            res = cursor_meta.fetchone()
            last_created = res[0] if res and res[0] else None
            dim_airline_existing = pd.read_sql_query("SELECT * FROM dim_airline", m_conn_meta)
            dim_airport_existing = pd.read_sql_query("SELECT * FROM dim_airport", m_conn_meta)
            dim_date_existing = pd.read_sql_query("SELECT * FROM dim_date", m_conn_meta)
        except Exception as query_err:
            print(f"Aviso: Error consultando MonetDB (quizás primera corrida): {query_err}")
            dim_airline_existing = pd.DataFrame(columns=['airline_key', 'carrier_code', 'airline_name'])
            dim_airport_existing = pd.DataFrame(columns=['airport_key', 'airport_code', 'city', 'state'])
            dim_date_existing = pd.DataFrame(columns=['date_key', 'fl_date', 'year', 'month', 'day_of_month', 'day_of_week', 'is_weekend'])
            
        m_conn_meta.close()
    except Exception as e:
        print(f"Aviso: No se pudo conectar a MonetDB: {e}")
        dim_airline_existing = pd.DataFrame(columns=['airline_key', 'carrier_code', 'airline_name'])
        dim_airport_existing = pd.DataFrame(columns=['airport_key', 'airport_code', 'city', 'state'])
        dim_date_existing = pd.DataFrame(columns=['date_key', 'fl_date', 'year', 'month', 'day_of_month', 'day_of_week', 'is_weekend'])

    # 1. Extracción desde PocketBase.flights_raw (SQLite)
    print(f"Conectando a PocketBase SQLite (buscando registros > {last_created if last_created else 'Inicio'})...")
    pb_conn = sqlite3.connect(PB_DB_PATH)
    
    query = "SELECT * FROM flights_raw"
    params = ()
    if last_created:
        query += " WHERE created > ?"
        params = (last_created,)
        
    df_raw = pd.read_sql_query(query, pb_conn, params=params)
    pb_conn.close()
    
    if df_raw.empty:
        print("No hay registros NUEVOS en PocketBase.flights_raw para procesar.")
        return
        
    print(f"Registros extraídos de Staging: {len(df_raw)}")

    # 2. Validación de Calidad de Datos (Circuit Breaker y Cuarentena)
    df_clean, df_quarantine, _ = DataValidator.validate_batch(df_raw)
    print(f"Registros limpios para cargar: {len(df_clean)}")
    print(f"Registros en cuarentena: {len(df_quarantine)}")

    if df_clean.empty:
        print("No hay registros válidos después de la validación. Cancelando ETL.")
        return

    # 3. Transformación (Modelo Dimensional / Star Schema)
    print("Generando dimensiones y tabla de hechos...")
    
    # dim_airline
    carriers = df_clean['op_unique_carrier'].unique()
    new_carriers = [c for c in carriers if c not in dim_airline_existing['carrier_code'].values]
    if new_carriers:
        max_airline_key = dim_airline_existing['airline_key'].max() if not dim_airline_existing.empty else 0
        carrier_names = {
            'AA': 'American Airlines', 'DL': 'Delta Air Lines', 'UA': 'United Airlines',
            'WN': 'Southwest Airlines', 'B6': 'JetBlue Airways', 'AS': 'Alaska Airlines',
            'NK': 'Spirit Airlines', 'F9': 'Frontier Airlines', 'HA': 'Hawaiian Airlines',
            'G4': 'Allegiant Air'
        }
        new_dim_airline = pd.DataFrame({
            'airline_key': range(max_airline_key + 1, max_airline_key + 1 + len(new_carriers)),
            'carrier_code': new_carriers,
            'airline_name': [carrier_names.get(c, f"Unknown Airline ({c})") for c in new_carriers]
        })
        dim_airline_full = pd.concat([dim_airline_existing, new_dim_airline])
    else:
        new_dim_airline = pd.DataFrame()
        dim_airline_full = dim_airline_existing

    # dim_airport
    origins = df_clean[['origin', 'origin_city_name', 'origin_state_nm']].rename(
        columns={'origin': 'airport_code', 'origin_city_name': 'city', 'origin_state_nm': 'state'}
    )
    dests = df_clean[['dest', 'dest_city_name', 'dest_state_nm']].rename(
        columns={'dest': 'airport_code', 'dest_city_name': 'city', 'dest_state_nm': 'state'}
    )
    airports = pd.concat([origins, dests]).drop_duplicates(subset=['airport_code'])
    new_airports = airports[~airports['airport_code'].isin(dim_airport_existing['airport_code'])]
    if not new_airports.empty:
        max_airport_key = dim_airport_existing['airport_key'].max() if not dim_airport_existing.empty else 0
        new_airports = new_airports.copy()
        new_airports['airport_key'] = range(max_airport_key + 1, max_airport_key + 1 + len(new_airports))
        new_dim_airport = new_airports[['airport_key', 'airport_code', 'city', 'state']]
        dim_airport_full = pd.concat([dim_airport_existing, new_dim_airport])
    else:
        new_dim_airport = pd.DataFrame()
        dim_airport_full = dim_airport_existing

    # dim_date
    dates = pd.to_datetime(df_clean['fl_date']).unique()
    date_strs = [d.strftime('%Y-%m-%d') for d in dates]
    new_dates = [d for d, d_str in zip(dates, date_strs) if d_str not in dim_date_existing['fl_date'].values]
    
    if new_dates:
        max_date_key = dim_date_existing['date_key'].max() if not dim_date_existing.empty else 0
        new_dim_date = pd.DataFrame({
            'date_key': range(max_date_key + 1, max_date_key + 1 + len(new_dates)),
            'fl_date': [d.strftime('%Y-%m-%d') for d in new_dates],
            'year': [d.year for d in new_dates],
            'month': [d.month for d in new_dates],
            'day_of_month': [d.day for d in new_dates],
            'day_of_week': [d.weekday() + 1 for d in new_dates],
            'is_weekend': [1 if d.weekday() >= 5 else 0 for d in new_dates]
        })
        dim_date_full = pd.concat([dim_date_existing, new_dim_date])
    else:
        new_dim_date = pd.DataFrame()
        dim_date_full = dim_date_existing

    # fact_flights (unir claves sustitutas)
    fact_flights = df_clean.copy()
    
    # Mapeos
    airline_map = dict(zip(dim_airline_full['carrier_code'], dim_airline_full['airline_key']))
    airport_map = dict(zip(dim_airport_full['airport_code'], dim_airport_full['airport_key']))
    date_map = dict(zip(dim_date_full['fl_date'], dim_date_full['date_key']))

    fact_flights['airline_key'] = fact_flights['op_unique_carrier'].map(airline_map)
    fact_flights['origin_key'] = fact_flights['origin'].map(airport_map)
    fact_flights['dest_key'] = fact_flights['dest'].map(airport_map)
    fact_flights['date_key'] = fact_flights['fl_date'].map(date_map)

    # Asegurarnos de traer el timestamp de creacion de PB
    if 'created' not in df_clean.columns:
        df_clean['created'] = None
    df_clean.rename(columns={'created': 'pb_created'}, inplace=True)
    
    # Conservar columnas de hechos + columnas extras para features
    fact_cols = [
        'id', 'pb_created', 'date_key', 'airline_key', 'origin_key', 'dest_key',
        'op_carrier_fl_num', 'dep_delay', 'arr_delay', 'cancelled',
        'cancellation_code', 'diverted', 'air_time', 'distance',
        'carrier_delay', 'weather_delay', 'nas_delay', 'late_aircraft_delay',
        # Campos extra guardados directamente para features en la fact table
        'taxi_out', 'wheels_off', 'wheels_on', 'taxi_in', 'crs_dep_time',
        'dep_time', 'crs_arr_time', 'arr_time', 'crs_elapsed_time',
        'actual_elapsed_time', 'security_delay'
    ]
    
    # Rellenar nulos numéricos con 0 para evitar errores de tipo en base de datos analítica
    num_cols = [
        'dep_delay', 'arr_delay', 'air_time', 'distance', 'carrier_delay',
        'weather_delay', 'nas_delay', 'late_aircraft_delay', 'taxi_out',
        'wheels_off', 'wheels_on', 'taxi_in', 'crs_dep_time', 'dep_time',
        'crs_arr_time', 'arr_time', 'crs_elapsed_time', 'actual_elapsed_time',
        'security_delay'
    ]
    for col in num_cols:
        if col in fact_flights.columns:
            fact_flights[col] = pd.to_numeric(fact_flights[col], errors='coerce').fillna(0)

    fact_flights = fact_flights[fact_cols]

    # 4. Carga a MonetDB
    print("Conectando a MonetDB...")
    try:
        m_conn = pymonetdb.connect(
            host=MONETDB_HOST,
            port=MONETDB_PORT,
            username=MONETDB_USER,
            password=MONETDB_PASS,
            database=MONETDB_DB
        )
        cursor = m_conn.cursor()

        # Crear tablas si no existen
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dim_airline (
                airline_key INT PRIMARY KEY,
                carrier_code VARCHAR(10),
                airline_name VARCHAR(100)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dim_airport (
                airport_key INT PRIMARY KEY,
                airport_code VARCHAR(10),
                city VARCHAR(100),
                state VARCHAR(100)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dim_date (
                date_key INT PRIMARY KEY,
                fl_date DATE,
                year INT,
                month INT,
                day_of_month INT,
                day_of_week INT,
                is_weekend INT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Quarantine_Data (
                id VARCHAR(50) PRIMARY KEY,
                pb_created TIMESTAMP,
                quarantine_reason VARCHAR(500),
                raw_json CLOB
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fact_flights (
                id VARCHAR(50) PRIMARY KEY,
                pb_created TIMESTAMP,
                date_key INT,
                airline_key INT,
                origin_key INT,
                dest_key INT,
                op_carrier_fl_num INT,
                dep_delay DOUBLE,
                arr_delay DOUBLE,
                cancelled INT,
                cancellation_code VARCHAR(5),
                diverted INT,
                air_time DOUBLE,
                distance DOUBLE,
                carrier_delay DOUBLE,
                weather_delay DOUBLE,
                nas_delay DOUBLE,
                late_aircraft_delay DOUBLE,
                taxi_out DOUBLE,
                wheels_off DOUBLE,
                wheels_on DOUBLE,
                taxi_in DOUBLE,
                crs_dep_time DOUBLE,
                dep_time DOUBLE,
                crs_arr_time DOUBLE,
                arr_time DOUBLE,
                crs_elapsed_time DOUBLE,
                actual_elapsed_time DOUBLE,
                security_delay DOUBLE
            );
        """)

        def bulk_insert_df(table_name, df):
            if df.empty:
                return
            # SE ELIMINÓ EL DELETE FROM PARA CARGA INCREMENTAL

            # Preparar inserción en lotes de 2000
            cols = ", ".join(df.columns)
            batch = []
            for _, row in df.iterrows():
                # Escapar strings
                vals = []
                for val in row:
                    if pd.isna(val):
                        vals.append("NULL")
                    elif isinstance(val, str):
                        vals.append(f"'{val.replace("'", "''")}'")
                    else:
                        vals.append(str(val))
                batch.append(f"({', '.join(vals)})")

                if len(batch) >= 2000:
                    cursor.execute(f"INSERT INTO {table_name} ({cols}) VALUES {', '.join(batch)}")
                    batch = []
            if batch:
                cursor.execute(f"INSERT INTO {table_name} ({cols}) VALUES {', '.join(batch)}")

        def bulk_insert_quarantine(df_quarantine: pd.DataFrame):
            if df_quarantine.empty:
                return
            cols = "id, pb_created, quarantine_reason, raw_json"
            batch = []
            for _, row in df_quarantine.iterrows():
                record_id = str(row.get('id', 'UNKNOWN'))
                pb_created = str(row.get('created', 'NULL'))
                reason = str(row.get('quarantine_reason', '')).replace("'", "''")
                raw_json = str(row.to_dict()).replace("'", "''")
                batch.append(f"('{record_id}', '{pb_created}', '{reason}', '{raw_json}')")

                if len(batch) >= 2000:
                    cursor.execute(f"INSERT INTO Quarantine_Data ({cols}) VALUES {', '.join(batch)}")
                    batch = []
            if batch:
                cursor.execute(f"INSERT INTO Quarantine_Data ({cols}) VALUES {', '.join(batch)}")
            print(f"[MONETDB] {len(df_quarantine)} registros en Quarantine_Data.")

        print("Cargando dim_airline (nuevas)...")
        bulk_insert_df("dim_airline", new_dim_airline)

        print("Cargando dim_airport (nuevas)...")
        bulk_insert_df("dim_airport", new_dim_airport)

        print("Cargando dim_date (nuevas)...")
        bulk_insert_df("dim_date", new_dim_date)

        print("Cargando fact_flights (nuevas)...")
        bulk_insert_df("fact_flights", fact_flights)

        print("Cargando Quarantine_Data...")
        bulk_insert_quarantine(df_quarantine)

        m_conn.commit()
        print("[MONETDB] Carga masiva exitosa.")
        
        # 5. Refrescar vistas materializadas para dashboards
        print("Creando/Refrescando vistas analíticas...")
        cursor.execute("""
            CREATE OR REPLACE VIEW vw_bsc_monthly AS
            SELECT 
                d.year, d.month,
                COUNT(*) AS total_flights,
                AVG(f.dep_delay) AS avg_dep_delay,
                SUM(f.cancelled) * 100.0 / COUNT(*) AS cancellation_rate
            FROM fact_flights f
            JOIN dim_date d ON f.date_key = d.date_key
            GROUP BY d.year, d.month;
        """)
        cursor.execute("""
            CREATE OR REPLACE VIEW vw_delay_analysis AS
            SELECT 
                f.id, d.year, d.month, d.day_of_week, d.is_weekend,
                a.carrier_code,
                f.dep_delay, f.arr_delay, f.distance, f.air_time,
                f.carrier_delay, f.weather_delay, f.nas_delay, f.late_aircraft_delay,
                f.taxi_out, f.crs_dep_time, d.fl_date
            FROM fact_flights f
            JOIN dim_date d ON f.date_key = d.date_key
            JOIN dim_airline a ON f.airline_key = a.airline_key;
        """)
        m_conn.commit()
        print("[MONETDB] Vistas analíticas listas.")
        
        m_conn.close()
        print("--- ETL FINALIZADO CON ÉXITO ---")

    except Exception as e:
        print(f"Error durante la carga en MonetDB: {e}")

if __name__ == "__main__":
    run_etl()
