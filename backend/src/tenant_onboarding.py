import sys
import os

# Asegurar que importamos los modulos correctamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Tenant
from src.services.api_key_service import ApiKeyService

def onboard_new_tenant(company_name: str, email: str, country: str = None) -> dict:
    """
    Orquesta el onboarding:
    1. Valida los datos y el correo usando Pydantic
    2. Si es válido, genera llaves
    3. Retorna un dict con los datos seguros simulando respuesta JSON
    """
    try:
        # 1. Validación (Lanzará ValueError si es un correo no corporativo)
        new_tenant = Tenant(
            company_name=company_name,
            contact_email=email,
            country=country
        )
        
        # 2. Aprovisionamiento de API Keys
        keys = ApiKeyService.generate_key_pair()
        
        live_key_plain = keys["live_key"]
        live_key_hash = ApiKeyService.hash_key(live_key_plain)
        
        test_key_plain = keys["test_key"]
        test_key_hash = ApiKeyService.hash_key(test_key_plain)
        
        # Simulamos que guardamos en la Base de Datos:
        # insert into Tenants (id, company, email, live_key_hash, test_key_hash) ...
        # (Aquí omitimos la conexión real de SQL para enfocarnos en la lógica)
        
        # 3. Respuesta al UI One-Time
        return {
            "success": True,
            "message": "Tenant registrado exitosamente. Por favor, guarde sus llaves (no se mostrarán de nuevo).",
            "data": {
                "tenant_id": new_tenant.id,
                "company_name": new_tenant.company_name,
                "test_key": test_key_plain, # One-time display
                "live_key": live_key_plain, # One-time display
                # Debug puro para ver que sí tenemos el hash
                "_internal_live_hash_stored": live_key_hash 
            }
        }
        
    except ValueError as e:
        # Fallo por validación Pydantic
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    # Prueba feliz
    print("--- Prueba 1: Corporativo Válido ---")
    res1 = onboard_new_tenant("Delta Airlines", "admin@delta.com", "US")
    print(res1)
    
    print("\n--- Prueba 2: Intento Fraudulento ---")
    res2 = onboard_new_tenant("Hacker Inc", "hacker@gmail.com", "RU")
    print(res2)
