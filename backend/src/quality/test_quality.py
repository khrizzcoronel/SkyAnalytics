import sys
import os

# Asegurar importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_quality_suite import DataQualitySuite, DataQualityThresholdError

def run_tests():
    suite = DataQualitySuite(tolerance_rate=0.01) # 1% max error
    
    # --- ESCENARIO 1: Lote Sano (pasa la prueba) ---
    print("\n--- TEST 1: Lote Staging Limpio (Schema Drift < 1%) ---")
    good_batch = [
        {"flight_id": "AA123", "departure_date": "2026-11-01", "airline": "AA", "status": "ON_TIME", "monto_pago": 150.0},
        {"flight_id": "DL456", "departure_date": "2026-11-01", "airline": "DL", "status": "DELAYED", "monto_pago": 200.0},
        {"flight_id": "UA789", "departure_date": "2026-11-01", "airline": "UA", "status": "CANCELLED", "monto_pago": 300.0},
    ]
    try:
        suite.run_suite(good_batch)
        print("Test 1: OK (Promovido correctamente)")
    except Exception as e:
        print(f"Test 1: FALLÓ inesperadamente - {e}")
        
    # --- ESCENARIO 2: Schema Drift masivo (falla duro) ---
    print("\n--- TEST 2: Lote con Schema Drift (> 1% errores) ---")
    bad_batch = [
        {"flight_id": "AA123", "departure_date": "2026-11-01", "airline": "AA", "status": "ON_TIME", "monto_pago": 150.0},
        # status INVENTADO (no está en el Enum Literal) -> Error Pydantic
        {"flight_id": "DL456", "departure_date": "2026-11-01", "airline": "DL", "status": "UNKNOWN", "monto_pago": 200.0},
        # monto_pago negativo -> Error Pydantic
        {"flight_id": "UA789", "departure_date": "2026-11-01", "airline": "UA", "status": "CANCELLED", "monto_pago": -50.0},
    ]
    
    # Aquí el error rate será 2/3 = 66% (Mucho mayor a 1%)
    try:
        suite.run_suite(bad_batch)
        print("Test 2: FALLÓ - No debió promover este lote.")
    except DataQualityThresholdError as e:
        print(f"Test 2: OK - Circuit Breaker activado correctamente.")
        print(f"Mensaje: {e}")

if __name__ == "__main__":
    run_tests()
