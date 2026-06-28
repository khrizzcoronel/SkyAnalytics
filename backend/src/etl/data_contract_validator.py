class DataContractValidator:
    def __init__(self, contract: dict):
        self.contract = contract

    def validate_schema(self, incoming_data: dict) -> bool:
        print("\n[SCHEMA REGISTRY] Validando datos entrantes contra Contrato (v1)...")
        
        # Verificar campos obligatorios del contrato
        for field, expected_type in self.contract.items():
            if field not in incoming_data:
                print(f"[SCHEMA REGISTRY] FALLO: Schema Violation. Falta el campo requerido '{field}'.")
                print(f"[ETL DLQ] Enviando registro corrupto a Dead Letter Queue (DLQ) para aislamiento.")
                return False
                
            actual_type = type(incoming_data[field]).__name__
            if actual_type != expected_type:
                print(f"[SCHEMA REGISTRY] FALLO: Schema Drift. Campo '{field}' esperaba '{expected_type}' pero recibio '{actual_type}'.")
                print(f"[ETL DLQ] Enviando registro corrupto a Dead Letter Queue (DLQ) para aislamiento.")
                return False
                
        # Campos extra (Forward compatible)
        extra_fields = set(incoming_data.keys()) - set(self.contract.keys())
        if extra_fields:
            print(f"[SCHEMA REGISTRY] ADVERTENCIA: Cambio Forward-Compatible detectado. Campos extra: {list(extra_fields)}")
            print("[SCHEMA REGISTRY] Actualizando version del Data Contract a v1.1. Ingestion permitida.")
        else:
            print("[SCHEMA REGISTRY] Validacion exitosa. Cumple contrato estrictamente.")
            
        return True

if __name__ == "__main__":
    base_contract = {
        "flight_number": "str",
        "delay_minutes": "int"
    }
    validator = DataContractValidator(base_contract)
    
    # Escenario 1: Forward Compatible (Nuevo campo opcional)
    print("--- Escenario 1: Forward Compatible ---")
    data_ok = {
        "flight_number": "AA123",
        "delay_minutes": 15,
        "wifi_available": True
    }
    validator.validate_schema(data_ok)
    
    # Escenario 2: Incompatible (Campo borrado)
    print("\n--- Escenario 2: Schema Drift Incompatible ---")
    data_bad = {
        "flight_id_hash": "a1b2c3d4",
        "delay_minutes": 15
    }
    validator.validate_schema(data_bad)
