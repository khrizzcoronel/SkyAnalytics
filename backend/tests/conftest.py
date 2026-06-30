import os

os.environ.setdefault("MONETDB_PASS", "dummy-test-password")

import pytest
from fastapi.testclient import TestClient

from src.api_server import app, get_auth_service, get_flight_repository
from src.security.secret_rotator import InMemorySecretStore, SecretRotator
from tests.helpers import FakeAuthService, FakeFlightRepository


@pytest.fixture
def client():
    app.dependency_overrides[get_auth_service] = lambda: FakeAuthService()
    app.dependency_overrides[get_flight_repository] = lambda: FakeFlightRepository()
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture
def rotator():
    return SecretRotator(InMemorySecretStore())
