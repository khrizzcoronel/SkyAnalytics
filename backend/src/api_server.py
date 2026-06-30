import os
import time
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any, Callable

import pymonetdb
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.services.tenant_auth_service import TenantAuthService, AuthenticationError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_server")

app = FastAPI(title="SkyAnalytics API Gateway", version="1.0.0")

# --- Configuration ---
MONETDB_HOST = os.getenv("MONETDB_HOST", "monetdb")
MONETDB_PORT = int(os.getenv("MONETDB_PORT", "50000"))
MONETDB_DATABASE = os.getenv("MONETDB_DATABASE", "skyanalytics")
MONETDB_USER = os.getenv("MONETDB_USER", "monetdb")
MONETDB_PASSWORD = os.getenv("MONETDB_PASSWORD")

RATE_LIMIT_MAX = int(os.getenv("DEFAULT_API_QUOTA", "1000"))
CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "300"))

# --- In-memory cache with TTL ---
_FAKE_CACHE: Dict[str, Dict[str, Any]] = {}


def _cache_get(key: str) -> Optional[Dict[str, Any]]:
    entry = _FAKE_CACHE.get(key)
    if not entry:
        return None
    if datetime.now(timezone.utc) > entry["expires_at"]:
        del _FAKE_CACHE[key]
        return None
    return entry["value"]


def _cache_set(key: str, value: Dict[str, Any], ttl: int = CACHE_TTL_SECONDS) -> None:
    _FAKE_CACHE[key] = {
        "value": value,
        "expires_at": datetime.now(timezone.utc) + timedelta(seconds=ttl),
    }


# --- Dependency factories (overridable in tests) ---
def get_auth_service() -> TenantAuthService:
    return TenantAuthService()


def get_flight_repository() -> "FlightRepository":
    return FlightRepository()


# --- Models ---
class FlightResponse(BaseModel):
    flight_id: str
    status: str
    prediction_delay_minutes: int
    cached: bool = False


# --- Repositories ---
class FlightRepository:
    """Lee vuelos de MonetDB; si falla, devuelve datos sintéticos para desarrollo."""

    def get_flight(self, flight_id: str) -> Optional[Dict[str, Any]]:
        try:
            if not MONETDB_PASSWORD:
                raise RuntimeError("MONETDB_PASSWORD not configured")
            conn = pymonetdb.connect(
                hostname=MONETDB_HOST,
                port=MONETDB_PORT,
                database=MONETDB_DATABASE,
                username=MONETDB_USER,
                password=MONETDB_PASSWORD,
            )
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT flight_id, status, prediction_delay_minutes
                FROM fact_flights
                WHERE flight_id = %s
                LIMIT 1
                """,
                (flight_id,),
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return {
                    "flight_id": row[0],
                    "status": row[1],
                    "prediction_delay_minutes": row[2] or 0,
                }
        except Exception as exc:
            logger.warning("MonetDB flight lookup failed: %s. Falling back to synthetic.", exc)
        return None

    def get_synthetic_flight(self, flight_id: str) -> Dict[str, Any]:
        # Determinista para tests/demos
        delay = (hash(flight_id) % 30) - 5
        status = "DELAYED" if delay > 10 else "ON_TIME"
        return {
            "flight_id": flight_id,
            "status": status,
            "prediction_delay_minutes": max(0, delay),
        }


# --- Dependencies ---
async def verify_api_key(
    x_api_key: str = Header(None),
    auth_service: TenantAuthService = Depends(get_auth_service),
) -> Dict[str, Any]:
    try:
        tenant = auth_service.verify_api_key(x_api_key)
    except AuthenticationError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc

    usage = auth_service.check_rate_limit(tenant["tenant_id"])
    if usage["remaining"] <= 0:
        raise HTTPException(
            status_code=429,
            detail="Monthly quota exceeded. Upgrade to Pro plan.",
        )

    auth_service.record_usage(tenant["tenant_id"])
    tenant["rate_limit_remaining"] = usage["remaining"] - 1
    return tenant


# --- Endpoints ---
@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/v1/flights/{flight_id}")
async def get_flight(
    flight_id: str,
    tenant: Dict[str, Any] = Depends(verify_api_key),
    repo: FlightRepository = Depends(get_flight_repository),
):
    cache_key = f"flight:{flight_id}"
    cached = _cache_get(cache_key)
    if cached:
        return {
            **cached,
            "cached": True,
            "rate_limit_remaining": tenant["rate_limit_remaining"],
        }

    # Simulación de procesamiento pesado (ML + DB)
    time.sleep(0.05)

    flight = repo.get_flight(flight_id)
    if flight is None:
        flight = repo.get_synthetic_flight(flight_id)

    _cache_set(cache_key, flight)

    return {
        **flight,
        "cached": False,
        "rate_limit_remaining": tenant["rate_limit_remaining"],
    }


# --- Error handlers ---
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
