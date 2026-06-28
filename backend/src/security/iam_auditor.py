class IAMAuditor:
    def audit_permission(self, role: str, permission: str, last_used_days: int):
        print(f"\n[IAM AUDITOR] Evaluando permiso '{permission}' del rol '{role}'. Ultimo uso: hace {last_used_days} dias.")
        
        if last_used_days > 90:
            print(f"[IAM AUDITOR] ALERTA: Permiso huerfano detectado (> 90 dias sin uso).")
            print(f"[IAM AUDITOR] REMEDIACION AUTOMATICA: Revocando política '{permission}' del rol '{role}'...")
            print(f"[IAM AUDITOR] Evento registrado en auditoria SOC 2.")
        else:
            print(f"[IAM AUDITOR] Permiso activo y en uso regular. Cumple Principio de Menor Privilegio.")

if __name__ == "__main__":
    auditor = IAMAuditor()
    auditor.audit_permission("Dev_Senior_Role", "s3:DeleteBucket", 180)
    auditor.audit_permission("Dev_Senior_Role", "rds:DescribeDBInstances", 14)
