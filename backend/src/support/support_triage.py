class BugTriageEngine:
    CRITICAL_KEYWORDS = ['500', 'crash', 'bloqueador', 'internal server error']

    def process_ticket(self, tenant_id: str, plan_type: str, description: str):
        print(f"\n--- NUEVO TICKET RECIBIDO [{tenant_id}] ---")
        
        is_critical = any(keyword in description.lower() for keyword in self.CRITICAL_KEYWORDS)
        
        severity = "S4" # Normal by default
        
        if plan_type.lower() == "enterprise":
            if is_critical:
                severity = "S1"
            else:
                severity = "S2"
        elif plan_type.lower() == "pro":
            severity = "S2" if is_critical else "S3"
            
        print(f"Clasificación automática: Nivel de Severidad {severity}")
        
        if severity == "S1":
            print(f"[ESCALAMIENTO SLACK] Bug Crítico (S1) para cliente Enterprise {tenant_id}. ¡SLA de resolución < 4 horas!")
        
        return severity

if __name__ == "__main__":
    engine = BugTriageEngine()
    
    # Simula cliente Freemium con bug menor
    engine.process_ticket("tenant_free", "freemium", "El boton de exportar esta desalineado")
    
    # Simula cliente Enterprise con caída total
    engine.process_ticket("tenant_corp", "enterprise", "Obtengo un 500 internal server error al consultar vuelos")
