class PeopleAnalytics:
    def calculate_enps(self, team_name: str, scores: list[int]):
        print(f"\n[PEOPLE ANALYTICS] Analizando eNPS para el equipo: {team_name}")
        
        # Regla CA-E06-002: Ocultar si hay menos de 3 respuestas (Privacidad)
        if len(scores) < 3:
            print("[PRIVACIDAD] Resultados ocultos (N/A) por riesgo de desanonimizacion (< 3 respuestas).")
            return None
            
        promoters = sum(1 for s in scores if s >= 9)
        detractors = sum(1 for s in scores if s <= 6)
        
        total = len(scores)
        pct_promoters = (promoters / total) * 100
        pct_detractors = (detractors / total) * 100
        
        enps = pct_promoters - pct_detractors
        print(f"[PEOPLE ANALYTICS] Respuestas: {total} | Promotores: {pct_promoters:.0f}% | Detractores: {pct_detractors:.0f}%")
        print(f"[PEOPLE ANALYTICS] Score eNPS: {enps:.1f}")
        
        # Alertas de riesgo
        if enps < 10:
            print("[ALERTA RRHH] [ROJO] Riesgo severo de Burnout/Fuga de Talento detectado.")
            print("[ALERTA RRHH] Recomendacion: Iniciar entrevistas 1:1 de retencion y revision de guardias on-call inmediatamente.")
            
        return enps

if __name__ == "__main__":
    analytics = PeopleAnalytics()
    
    # Escenario 1: Privacidad (Pocas respuestas)
    analytics.calculate_enps("Legal", [10, 8])
    
    # Escenario 2: Equipo sano
    analytics.calculate_enps("Data Science", [9, 10, 10, 8, 9, 7, 10])
    
    # Escenario 3: Riesgo de Burnout
    analytics.calculate_enps("SRE (On-Call)", [5, 4, 7, 8, 2, 6, 9])
