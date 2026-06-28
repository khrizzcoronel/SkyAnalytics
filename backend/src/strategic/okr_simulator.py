class OKRSimulator:
    def __init__(self, current_arr: float):
        self.current_arr = current_arr
        self.published_okrs = []

    def simulate_arr(self, churn_rate: float, new_customers_mrr: float) -> float:
        print("\n[WHAT-IF ENGINE] Ejecutando proyecciones financieras para Q4...")
        
        if churn_rate < 0:
            print("[WHAT-IF ENGINE] ERROR: El Churn Rate no puede ser negativo.")
            return self.current_arr
            
        # Simulación simplificada de impacto
        churn_impact = self.current_arr * churn_rate
        projected_arr = self.current_arr - churn_impact + (new_customers_mrr * 12)
        
        print(f"[WHAT-IF ENGINE] ARR Actual: ${self.current_arr:,.2f}")
        print(f"[WHAT-IF ENGINE] Impacto Churn ({churn_rate*100}%): -${churn_impact:,.2f}")
        print(f"[WHAT-IF ENGINE] ARR Proyectado: ${projected_arr:,.2f}")
        
        return projected_arr

    def publish_okr(self, objective: str, key_results: list[str], assignee: str):
        if not key_results:
            print("[OKR MANAGER] ERROR: La regla RN-E05-001 requiere al menos 1 Key Result cuantitativo.")
            return False
            
        okr = {
            "objective": objective,
            "key_results": key_results,
            "assignee": assignee,
            "status": "Activo"
        }
        self.published_okrs.append(okr)
        
        print(f"\n[OKR MANAGER] OKR Aprobado y Publicado: '{objective}'")
        print(f"[SLACK INTEGRATION] Enviando notificacion a #anuncios-globales...")
        print(f"   [SLACK] @{assignee} es el nuevo owner del objetivo estrategico. KRs asociados: {len(key_results)}")
        
        return True

if __name__ == "__main__":
    simulator = OKRSimulator(current_arr=5000000.0) # $5M ARR Base
    
    # Simular impacto de retencion
    simulator.simulate_arr(churn_rate=0.005, new_customers_mrr=50000.0)
    
    # Establecer OKRs basados en la simulacion
    simulator.publish_okr(
        objective="Dominar el mercado Enterprise Europeo",
        key_results=[
            "Reducir churn al 0.5% en Q4",
            "Cerrar 3 deals con aerolineas bandera"
        ],
        assignee="VP_Customer_Success"
    )
