import sys
import os
import requests

# Asegurar que importamos los modulos correctamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Tenant
from src.services.api_key_service import ApiKeyService

POCKETBASE_URL = os.getenv("POCKETBASE_URL", "http://pocketbase:8090")
POCKETBASE_ADMIN_EMAIL = os.getenv("POCKETBASE_ADMIN_EMAIL")
POCKETBASE_ADMIN_PASSWORD = os.getenv("POCKETBASE_ADMIN_PASSWORD")


def _get_admin_token() -> str:
    """Obtiene un token JWT de admin de PocketBase."""
    if not POCKETBASE_ADMIN_EMAIL or not POCKETBASE_ADMIN_PASSWORD:
        raise RuntimeError("POCKETBASE_ADMIN_EMAIL y POCKETBASE_ADMIN_PASSWORD son requeridos")

    resp = requests.post(
        f"{POCKETBASE_URL}/api/collections/_superusers/auth-with-password",
        json={"identity": POCKETBASE_ADMIN_EMAIL, "password": POCKETBASE_ADMIN_PASSWORD},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["token"]


def _create_tenant_record(token: str, payload: dict) -> str:
    """Crea el registro del tenant en PocketBase y devuelve su id."""
    resp = requests.post(
        f"{POCKETBASE_URL}/api/collections/tenants/records",
        json=payload,
        headers={"Authorization": token},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["id"]


def onboard_new_tenant(company_name: str, email: str, country: str = None) -> dict:
    """
    Orquesta el onboarding:
    1. Valida los datos y el correo usando Pydantic
    2. Genera API Keys y las hashea
    3. Persiste el tenant en PocketBase via HTTP API
    4. Retorna un dict con los datos seguros (one-time display)
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

        # 3. Persistencia real en PocketBase
        token = _get_admin_token()
        tenant_id = _create_tenant_record(
            token,
            {
                "company_name": new_tenant.company_name,
                "contact_email": new_tenant.contact_email,
                "country": new_tenant.country or "",
                "status": "active",
                "live_key_hash": live_key_hash,
                "test_key_hash": test_key_hash,
            },
        )

        # 4. Respuesta al UI One-Time
        return {
            "success": True,
            "message": "Tenant registrado exitosamente. Por favor, guarde sus llaves (no se mostrarán de nuevo).",
            "data": {
                "tenant_id": tenant_id,
                "company_name": new_tenant.company_name,
                "test_key": test_key_plain,  # One-time display
                "live_key": live_key_plain,  # One-time display
            }
        }

    except ValueError as e:
        # Fallo por validación Pydantic
        return {"success": False, "error": str(e)}
    except requests.HTTPError as e:
        return {"success": False, "error": f"Error persistiendo tenant: {e}"}
    except RuntimeError as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    # Prueba feliz
    print("--- Prueba 1: Corporativo Válido ---")
    res1 = onboard_new_tenant("Delta Airlines", "admin@delta.com", "US")
    print(res1)

    print("\n--- Prueba 2: Intento Fraudulento ---")
    res2 = onboard_new_tenant("Hacker Inc", "hacker@gmail.com", "RU")
    print(res2)
