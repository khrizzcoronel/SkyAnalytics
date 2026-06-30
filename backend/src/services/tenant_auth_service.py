import os
from datetime import datetime, timezone
from typing import Optional, Dict, Any
import requests
from passlib.hash import pbkdf2_sha256

POCKETBASE_URL = os.getenv("POCKETBASE_URL", "http://pocketbase:8090")
POCKETBASE_ADMIN_EMAIL = os.getenv("POCKETBASE_ADMIN_EMAIL")
POCKETBASE_ADMIN_PASSWORD = os.getenv("POCKETBASE_ADMIN_PASSWORD")

DEFAULT_MONTHLY_QUOTA = int(os.getenv("DEFAULT_API_QUOTA", "1000"))


class TenantAuthService:
    """
    Verifica API Keys contra PocketBase y controla rate-limit por tenant.
    Diseñado para ser inyectado en api_server y reemplazable en tests.
    """

    def __init__(
        self,
        base_url: str = POCKETBASE_URL,
        admin_email: Optional[str] = POCKETBASE_ADMIN_EMAIL,
        admin_password: Optional[str] = POCKETBASE_ADMIN_PASSWORD,
        quota: int = DEFAULT_MONTHLY_QUOTA,
    ):
        self.base_url = base_url.rstrip("/")
        self.admin_email = admin_email
        self.admin_password = admin_password
        self.quota = quota
        self._admin_token: Optional[str] = None

    def _get_admin_token(self) -> str:
        if self._admin_token:
            return self._admin_token
        if not self.admin_email or not self.admin_password:
            raise RuntimeError("PocketBase admin credentials not configured")
        resp = requests.post(
            f"{self.base_url}/api/collections/_superusers/auth-with-password",
            json={"identity": self.admin_email, "password": self.admin_password},
            timeout=10,
        )
        resp.raise_for_status()
        self._admin_token = resp.json()["token"]
        return self._admin_token

    def _find_tenant_by_key(self, api_key: str) -> Optional[Dict[str, Any]]:
        """Busca un tenant cuyo live_key_hash o test_key_hash coincida con la key."""
        # Optimización: PocketBase no permite filtrar por hash, así que paginamos.
        token = self._get_admin_token()
        headers = {"Authorization": token}
        page = 1
        while True:
            resp = requests.get(
                f"{self.base_url}/api/collections/tenants/records",
                headers=headers,
                params={"page": page, "perPage": 100},
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
            for item in data.get("items", []):
                for field in ("live_key_hash", "test_key_hash"):
                    hashed = item.get(field)
                    if hashed and pbkdf2_sha256.verify(api_key, hashed):
                        return item
            if page >= data.get("totalPages", 1):
                break
            page += 1
        return None

    def verify_api_key(self, api_key: Optional[str]) -> Dict[str, Any]:
        """Autentica la key. Retorna dict con tenant_id y entorno. Lanza excepción si falla."""
        if not api_key:
            raise AuthenticationError("Missing x-api-key header")
        tenant = self._find_tenant_by_key(api_key)
        if not tenant:
            raise AuthenticationError("Invalid API key")
        if tenant.get("status") != "active":
            raise AuthenticationError("Tenant is not active")
        return {
            "tenant_id": tenant["id"],
            "company_name": tenant.get("company_name"),
            "environment": "live" if api_key.startswith("sk_live_") else "test",
        }

    def check_rate_limit(self, tenant_id: str) -> Dict[str, int]:
        """Calcula uso actual y remanente del mes para un tenant."""
        # En producción esto debería leer Redis o una tabla de uso.
        # Por ahora usamos contador en memoria (TTL manual por mes).
        now = datetime.now(timezone.utc)
        bucket = f"{tenant_id}:{now.year}:{now.month}"
        used = _IN_MEMORY_USAGE.get(bucket, 0)
        remaining = max(0, self.quota - used)
        return {"used": used, "remaining": remaining, "limit": self.quota}

    def record_usage(self, tenant_id: str) -> None:
        now = datetime.now(timezone.utc)
        bucket = f"{tenant_id}:{now.year}:{now.month}"
        _IN_MEMORY_USAGE[bucket] = _IN_MEMORY_USAGE.get(bucket, 0) + 1


class AuthenticationError(Exception):
    pass


# Contador en memoria. En producción reemplazar por Redis/caché distribuida.
_IN_MEMORY_USAGE: Dict[str, int] = {}
