import re

class SecurityScanner:
    def scan_secrets(self, file_content: str) -> bool:
        print("\n[SAST SCANNER] Buscando credenciales hardcodeadas (Secret Leaks)...")
        
        # Regex simple para encontrar "password=", "secret=", "api_key=" seguido de comillas
        pattern = r'(password|secret|api_key|token)\s*=\s*[\'"][^\'"]+[\'"]'
        
        matches = re.findall(pattern, file_content, re.IGNORECASE)
        if matches:
            print(f"[SAST SCANNER] FALLO: Secret Leak Detected. Tipo(s): {matches}")
            print(f"[SAST SCANNER] Accion: Pipeline abortado. Notificando a DevSecOps.")
            return False
            
        print("[SAST SCANNER] Pass. No se encontraron secretos.")
        return True

    def scan_dependencies(self, dependencies: list[str]) -> bool:
        print("\n[SCA SCANNER] Analizando vulnerabilidades en dependencias de terceros (CVEs)...")
        
        # Simulación de base de datos de CVEs críticos (Snyk)
        vulnerable_packages = {
            "requests==2.10.0": "CVE-2026-XYZ Critico: Ejecucion de codigo remoto."
        }
        
        for dep in dependencies:
            if dep in vulnerable_packages:
                print(f"[SCA SCANNER] FALLO: Dependencia vulnerable detectada: '{dep}'.")
                print(f"[SCA SCANNER] Detalle: {vulnerable_packages[dep]}")
                print(f"[SCA SCANNER] Accion: Pipeline bloqueado. Por favor, actualice la libreria.")
                return False
                
        print("[SCA SCANNER] Pass. No se detectaron vulnerabilidades conocidas (0 CVEs criticos).")
        return True

if __name__ == "__main__":
    scanner = SecurityScanner()
    
    # Escenario 1: Secret Leak
    bad_code = """
    def connect_db():
        db_password = "super_secret_password_123"
        return db_password
    """
    scanner.scan_secrets(bad_code)
    
    # Escenario 2: Paquete Vulnerable
    bad_deps = ["flask==2.0.1", "requests==2.10.0", "numpy==1.21.0"]
    scanner.scan_dependencies(bad_deps)
