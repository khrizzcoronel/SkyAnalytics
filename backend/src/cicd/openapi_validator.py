import re

class OpenAPIValidator:
    def check_style(self, schema: dict) -> bool:
        print("\n[SPECTRAL LINTER] Ejecutando analisis de estilo (Style Guide)...")
        passed = True
        
        for prop in schema.get("properties", {}).keys():
            # Check for camelCase (simple check: has uppercase letters)
            if any(c.isupper() for c in prop):
                print(f"[SPECTRAL LINTER] ERROR: La propiedad '{prop}' rompe la convencion. Debe usar snake_case.")
                passed = False
                
        if not schema.get("description"):
            print("[SPECTRAL LINTER] ERROR: Documentacion obligatoria faltante. Falta 'description'.")
            passed = False
            
        return passed

    def check_backward_compatibility(self, old_schema: dict, new_schema: dict) -> bool:
        print("\n[OPENAPI-DIFF] Comparando rama actual contra main...")
        passed = True
        
        old_required = set(old_schema.get("required", []))
        new_required = set(new_schema.get("required", []))
        
        # If an old required field is missing in new schema properties
        new_props = new_schema.get("properties", {}).keys()
        for req in old_required:
            if req not in new_props:
                print(f"[OPENAPI-DIFF] ALERTA ROJA: Breaking Change detectado. Se elimino el campo obligatorio '{req}'.")
                print("[OPENAPI-DIFF] Bloqueando el Merge automatico. Por favor versione su API a v2.")
                passed = False
                
        return passed

if __name__ == "__main__":
    validator = OpenAPIValidator()
    
    # Escenario 2: Validacion de estilo fallida
    bad_style_schema = {
        "properties": {
            "flightDetails": {"type": "string"},
            "delay_minutes": {"type": "integer"}
        }
        # missing description
    }
    validator.check_style(bad_style_schema)
    
    # Escenario 1: Breaking change detectado
    old_schema = {
        "required": ["id", "delay_minutes"],
        "properties": {
            "id": {"type": "string"},
            "delay_minutes": {"type": "integer"}
        }
    }
    
    new_schema_breaking = {
        "required": ["id"],
        "properties": {
            "id": {"type": "string"}
            # delay_minutes eliminado
        }
    }
    validator.check_backward_compatibility(old_schema, new_schema_breaking)
