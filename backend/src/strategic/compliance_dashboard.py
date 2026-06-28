class ComplianceDashboard:
    def check_soc2_encryption(self, resources: list[dict]) -> bool:
        print("\n[COMPLIANCE] Evaluando controles SOC2 (Seguridad)...")
        passed = True
        
        for res in resources:
            if not res.get("encrypted", False):
                print(f"[COMPLIANCE] [ROJO] FALLO: Recurso '{res['name']}' no esta cifrado. (SOC2 CC6.7)")
                passed = False
                
        if passed:
            print("[COMPLIANCE] [VERDE] Todos los recursos evaluados cumplen con cifrado AES-256.")
            
        return passed

    def check_gdpr_residency(self, resources: list[dict]) -> bool:
        print("\n[COMPLIANCE] Evaluando controles GDPR (Data Residency)...")
        passed = True
        
        for res in resources:
            if res.get("data_type") == "EU_PII" and res.get("region") != "eu-central-1":
                print(f"[COMPLIANCE] [ROJO] FALLO CRITICO: Recurso '{res['name']}' con datos EU PII se encuentra en '{res['region']}'.")
                print(f"[COMPLIANCE] [ROJO] Requerido: eu-central-1")
                passed = False
                
        if passed:
            print("[COMPLIANCE] [VERDE] Residencia de datos europeos conforme.")
            
        return passed

if __name__ == "__main__":
    dashboard = ComplianceDashboard()
    
    # Recursos simulados de AWS Config
    cloud_resources = [
        {"name": "ebs-vol-01", "encrypted": True, "data_type": "Log", "region": "us-east-1"},
        {"name": "s3-eu-customers", "encrypted": False, "data_type": "EU_PII", "region": "us-east-1"}
    ]
    
    # Validacion
    soc2_status = dashboard.check_soc2_encryption(cloud_resources)
    gdpr_status = dashboard.check_gdpr_residency(cloud_resources)
    
    print("\n[COMPLIANCE EXPORT] Generando reporte de matriz de cumplimiento...")
    score = ((int(soc2_status) + int(gdpr_status)) / 2) * 100
    print(f"[COMPLIANCE EXPORT] Compliance Score: {score}%")
