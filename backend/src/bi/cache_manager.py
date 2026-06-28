import time

class BICacheManager:
    """
    Gestor encargado de mantener los dashboards BI rápidos 
    mediante vistas materializadas y cachés.
    """
    
    def refresh_materialized_view(self, tenant_id: str):
        """
        Simula un comando SQL que actualiza los datos pre-calculados sin bloquear.
        """
        print(f"[{tenant_id}] INICIANDO REFRESCO OLAP...")
        print(f"[{tenant_id}] Ejecutando: REFRESH MATERIALIZED VIEW CONCURRENTLY mv_dashboard_{tenant_id};")
        
        # Simula un ligero delay de cómputo en BD
        time.sleep(0.5)
        
        print(f"[{tenant_id}] Vistas materializadas actualizadas exitosamente.")
        return True

    def purge_bi_cache(self, tenant_id: str):
        """
        Simula una petición HTTP a la API de Superset/Metabase para borrar
        la memoria RAM temporal y obligar a leer de la nueva vista materializada.
        """
        print(f"[{tenant_id}] PURGANDO CACHÉ DE PRESENTACIÓN...")
        print(f"[{tenant_id}] [POST] http://bi-server.internal/api/v1/cache/clear?tenant={tenant_id}")
        
        # Simula delay de red
        time.sleep(0.2)
        
        print(f"[{tenant_id}] Caché purgada. El dashboard ahora cargará datos frescos en < 1.5s.\n")
        return True

def run_post_etl_refresh(tenants: list[str]):
    manager = BICacheManager()
    print("=== INICIANDO TAREAS POST-ETL (BI CACHE MANAGER) ===\n")
    
    for tenant in tenants:
        try:
            # 1. Base de datos: Pre-calcular sumas/promedios0
            manager.refresh_materialized_view(tenant)
            
            # 2. Capa UI: Borrar caché para que renderice los nuevos pre-cálculos
            manager.purge_bi_cache(tenant)
        except Exception as e:
            print(f"[{tenant}] ERROR al refrescar BI: {e}")
            # Falla controlada: El usuario verá caché Stale (Regla RN-O06-002)

if __name__ == "__main__":
    # Prueba de Aislamiento
    # Refrescamos tenants independientes, sin cruzar información
    test_tenants = ["tenant_123_delta", "tenant_456_american"]
    run_post_etl_refresh(test_tenants)