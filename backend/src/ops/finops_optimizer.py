class FinOpsOptimizer:
    def evaluate_pr_cost(self, increment_usd: float, budget_usd: float) -> bool:
        print(f"\n[INFRACOST] Calculando impacto financiero del PR...")
        print(f"[INFRACOST] Incremento estimado: ${increment_usd} | Presupuesto mensual: ${budget_usd}")
        
        threshold = budget_usd * 0.10
        if increment_usd > threshold:
            print(f"[FINOPS GATE] ALERTA: El PR incrementa los costos en mas del 10% permitido (${threshold}).")
            print("[FINOPS GATE] Accion: Requerida revision y aprobacion manual del Manager.")
            return False
            
        print("[FINOPS GATE] Pass. Gasto dentro de limites esperados.")
        return True

    def snooze_environments(self, instances: list[dict]):
        print(f"\n[GARBAGE COLLECTOR] Iniciando rutina de Snoozing de fin de semana (Viernes 19:00)...")
        
        for inst in instances:
            name = inst.get("name")
            env = inst.get("Environment", "Unknown")
            snooze_exempt = inst.get("FinOps-Snooze") == "False"
            
            if env == "Production":
                print(f"[GARBAGE COLLECTOR] Ignorando '{name}' (Entorno Produccion intocable).")
                continue
                
            if env == "Dev":
                if snooze_exempt:
                    print(f"[GARBAGE COLLECTOR] Ignorando '{name}' (Tiene excepcion FinOps-Snooze=False).")
                else:
                    print(f"[GARBAGE COLLECTOR] Apagando instancia '{name}' para ahorrar costos.")
                    
if __name__ == "__main__":
    optimizer = FinOpsOptimizer()
    
    # Escenario 1: Evaluacion Infracost en un PR muy costoso
    optimizer.evaluate_pr_cost(1200.0, 10000.0)
    
    # Escenario 2: Snoozing de fin de semana
    cloud_instances = [
        {"name": "api-prod-node-1", "Environment": "Production"},
        {"name": "db-dev-replica", "Environment": "Dev"},
        {"name": "data-science-gpu", "Environment": "Dev", "FinOps-Snooze": "False"}
    ]
    optimizer.snooze_environments(cloud_instances)
