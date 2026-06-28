class DisasterRecoveryDrill:
    def __init__(self, rto_limit_mins: int = 15):
        self.rto_limit_mins = rto_limit_mins

    def run_drill(self, simulated_restoration_time_mins: int):
        print("\n--- INICIANDO SIMULACRO DE DESASTRE (DR DRILL) ---")
        print(f"[AWS RDS] Restaurando DB desde el último Snapshot en VPC aislada...")
        print(f"[AWS RDS] Operación finalizada. Tiempo tomado: {simulated_restoration_time_mins} minutos.")
        
        print("[DATA INTEGRITY] Validando checksums y conteo de filas... OK.")
        
        if simulated_restoration_time_mins <= self.rto_limit_mins:
            print(f"[RTO CUMPLIDO] La restauración tomó {simulated_restoration_time_mins} min (Límite: {self.rto_limit_mins} min).")
            print("Resultado: PASSED. Certificación SOC 2 mantenida.")
        else:
            print(f"[RTO VIOLADO] La restauración tomó {simulated_restoration_time_mins} min, excediendo el límite de {self.rto_limit_mins} min.")
            print("[SLACK ALERT] El DR Drill ha fallado por lentitud. SRE debe incrementar IOPS del Snapshot inmediatamente.")
            
        print("[CLEANUP] Destruyendo entorno aislado...\n")

if __name__ == "__main__":
    drill = DisasterRecoveryDrill()
    
    # Escenario 1: Exitoso
    drill.run_drill(simulated_restoration_time_mins=11)
    
    # Escenario 2: Fallo de RTO
    drill.run_drill(simulated_restoration_time_mins=18)
