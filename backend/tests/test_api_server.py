import pytest
from fastapi.testclient import TestClient
from src.api_server import app, get_auth_service
from tests.helpers import FakeAuthService


VALID_KEY = "sk_live_validkey"


def test_health_check(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_flight_requires_api_key(client: TestClient):
    response = client.get("/v1/flights/AA123")
    assert response.status_code == 401
    assert "Missing" in response.json()["detail"]


def test_get_flight_invalid_key(client: TestClient):
    response = client.get("/v1/flights/AA123", headers={"x-api-key": "bad-key"})
    assert response.status_code == 401


def test_get_flight_success(client: TestClient):
    response = client.get(
        "/v1/flights/AA123",
        headers={"x-api-key": VALID_KEY},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["flight_id"] == "AA123"
    assert "prediction_delay_minutes" in data
    assert data["cached"] is False
    assert data["rate_limit_remaining"] >= 0


def test_rate_limit(client: TestClient):
    # Reducimos la quota para forzar el 429 rápidamente
    auth = FakeAuthService()
    auth.quota = 2
    app.dependency_overrides[get_auth_service] = lambda: auth
    try:
        client.get("/v1/flights/AA123", headers={"x-api-key": VALID_KEY})
        client.get("/v1/flights/AA123", headers={"x-api-key": VALID_KEY})
        response = client.get("/v1/flights/AA123", headers={"x-api-key": VALID_KEY})
        assert response.status_code == 429
        assert "quota" in response.json()["detail"].lower()
    finally:
        app.dependency_overrides.clear()
