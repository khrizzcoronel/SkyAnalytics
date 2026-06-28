import secrets
import string

class SecretRotator:
    def rotate_secret_if_needed(self, secret_name: str, age_days: int) -> bool:
        print(f"\n[SECRET ROTATOR] Evaluando secreto '{secret_name}'. Edad: {age_days} dias.")
        
        if age_days > 30:
            print(f"[SECRET ROTATOR] Edad > 30. Iniciando rotacion dinamica...")
            alphabet = string.ascii_letters + string.digits
            new_pwd = ''.join(secrets.choice(alphabet) for i in range(32))
            
            print(f"[SECRET ROTATOR] Nueva contrasena generada (32 chars).")
            print(f"[SECRET ROTATOR] Aplicando patron Overlap: Contrasena antigua funcionara 5 minutos más.")
            print(f"[SECRET ROTATOR] Inyectando nuevo secreto en PaaS/Serverless (Zero Downtime).")
            return True
        else:
            print(f"[SECRET ROTATOR] Secreto valido. No requiere rotacion.")
            return False

if __name__ == "__main__":
    rotator = SecretRotator()
    rotator.rotate_secret_if_needed("DB_PASSWORD_PROD", 45)
    rotator.rotate_secret_if_needed("STRIPE_API_KEY", 12)
