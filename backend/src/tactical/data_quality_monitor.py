class DataQualityMonitor:
    def validate_schema(self, data_batch: list[dict]) -> bool:
        print("\n[DATA QUALITY] Iniciando validacion de datos (Circuit Breaker)...")
        
        valid = True
        for index, row in enumerate(data_batch):
            # Regla RN-T04-002: Null check on flight_id
            if "flight_id" not in row or row["flight_id"] is None:
                print(f"[DATA QUALITY] [ROJO] Fila {index} aislada en cuarentena. Causa: Schema Drift o 'flight_id' nulo.")
                valid = False
                
        if not valid:
            print("[SLACK NOTIFICATION] Enviando alerta a #data-ops: Circuit Breaker accionado. Pipeline ETL detenido para prevenir corrupcion.")
            return False
            
        print("[DATA QUALITY] [VERDE] Validacion exitosa. Datos fusionados con el Data Warehouse.")
        return True

if __name__ == "__main__":
    monitor = DataQualityMonitor()
    
    # Escenario 1: Datos Limpios
    print("--- Escenario 1: Ejecucion Limpia ---")
    clean_data = [
        {"flight_id": "DL123", "departure": "2026-07-01T10:00"},
        {"flight_id": "UA456", "departure": "2026-07-01T12:00"}
    ]
    monitor.validate_schema(clean_data)
    
    # Escenario 2: Datos Corruptos
    print("\n--- Escenario 2: Schema Drift ---")
    corrupted_data = [
        {"flight_id": "AA789", "departure": "2026-07-01T15:00"},
        {"flight_id": None, "departure": "2026-07-01T18:00"} # Invalid
    ]
    monitor.validate_schema(corrupted_data)
