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
        {"fl_date": "2024-01-01", "op_unique_carrier": "AA", "op_carrier_fl_num": 123, "distance": 500, "dep_delay": -5},
        {"fl_date": "2024-01-01", "op_unique_carrier": "DL", "op_carrier_fl_num": 456, "distance": 1200, "dep_delay": 15},
        {"fl_date": "2024-01-01", "op_unique_carrier": "UA", "op_carrier_fl_num": 789, "distance": 300, "dep_delay": 0},
    ]
    try:
        suite.run_suite(good_batch, quarantine_path="./test_quarantine.csv")
        print("Test 1: OK (Promovido correctamente)")
    except Exception as e:
        print(f"Test 1: FALLÓ inesperadamente - {e}")
        
    # --- ESCENARIO 2: Schema Drift masivo (falla duro) ---
    print("\n--- TEST 2: Lote con Schema Drift (> 1% errores) ---")
    bad_batch = [
        # Fila correcta
        {"fl_date": "2024-01-01", "op_unique_carrier": "AA", "op_carrier_fl_num": 123, "distance": 500, "dep_delay": -5},
        # fl_date vacío -> Error en DataValidator
        {"fl_date": "", "op_unique_carrier": "DL", "op_carrier_fl_num": 456, "distance": 1200, "dep_delay": 15},
        # distance <= 0 -> Error en DataValidator
        {"fl_date": "2024-01-01", "op_unique_carrier": "UA", "op_carrier_fl_num": 789, "distance": -50, "dep_delay": 0},
    ]
    
    # Aquí el error rate será 2/3 = 66% (Mucho mayor a 1%)
    try:
        suite.run_suite(bad_batch, quarantine_path="./test_quarantine_bad.csv")
        print("Test 2: FALLÓ - No debió promover este lote.")
    except DataQualityThresholdError as e:
        print(f"Test 2: OK - Circuit Breaker activado correctamente.")
        print(f"Mensaje: {e}")
        
    # Limpiar archivos de prueba
    if os.path.exists("./test_quarantine.csv"):
        os.remove("./test_quarantine.csv")
    if os.path.exists("./test_quarantine_bad.csv"):
        os.remove("./test_quarantine_bad.csv")

if __name__ == "__main__":
    run_tests()
