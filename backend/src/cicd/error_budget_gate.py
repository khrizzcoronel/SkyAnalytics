def check_deployment_allowed(budget_consumed_percent: float, pr_label: str) -> bool:
    print(f"\n[CI/CD GATEKEEPER] Evaluando Pull Request. Etiqueta: '{pr_label}' | Error Budget Consumido: {budget_consumed_percent}%")
    
    if budget_consumed_percent > 80.0:
        if any(x in pr_label.lower() for x in ["hotfix", "reliability"]):
            print(f"[CI/CD GATEKEEPER] FEATURE FREEZE ACTIVO (>80%). Se permite el paso por excepcion '{pr_label}'.")
            return True
        else:
            print(f"[CI/CD GATEKEEPER] FEATURE FREEZE ACTIVO (>80%). Bloqueando PR '{pr_label}'. Solo se admiten hotfixes.")
            return False
    else:
        print(f"[CI/CD GATEKEEPER] Error Budget en niveles seguros. Despliegue permitido.")
        return True

if __name__ == "__main__":
    # Escenario 1: Normal, budget bien
    check_deployment_allowed(40.0, "feature/nuevo-dashboard")
    
    # Escenario 2: Feature bloqueado por budget
    check_deployment_allowed(85.0, "feature/nuevo-dashboard")
    
    # Escenario 3: Hotfix permitido a pesar del budget
    check_deployment_allowed(90.0, "hotfix/fuga-memoria")
