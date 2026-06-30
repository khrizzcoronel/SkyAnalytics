from src.services.tenant_auth_service import TenantAuthService, AuthenticationError
from src.api_server import FlightRepository


class FakeAuthService(TenantAuthService):
    def __init__(self, valid_key: str = "sk_live_validkey", tenant_id: str = "tenant_123"):
        super().__init__()
        self.valid_key = valid_key
        self.tenant_id = tenant_id
        self._usage = {}

    def verify_api_key(self, api_key):
        if not api_key:
            raise AuthenticationError("Missing x-api-key header")
        if api_key != self.valid_key:
            raise AuthenticationError("Invalid API key")
        return {
            "tenant_id": self.tenant_id,
            "company_name": "Acme",
            "environment": "live",
        }

    def check_rate_limit(self, tenant_id):
        used = self._usage.get(tenant_id, 0)
        return {"used": used, "remaining": self.quota - used, "limit": self.quota}

    def record_usage(self, tenant_id):
        self._usage[tenant_id] = self._usage.get(tenant_id, 0) + 1


class FakeFlightRepository(FlightRepository):
    def __init__(self, flight_id: str = "AA123", status: str = "ON_TIME", delay: int = 5):
        self.flight = {
            "flight_id": flight_id,
            "status": status,
            "prediction_delay_minutes": delay,
        }

    def get_flight(self, flight_id: str):
        return self.flight if flight_id == self.flight["flight_id"] else None

    def get_synthetic_flight(self, flight_id: str):
        return {
            "flight_id": flight_id,
            "status": "ON_TIME",
            "prediction_delay_minutes": 0,
        }
