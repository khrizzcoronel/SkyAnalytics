import importlib
import os
import pytest
from unittest.mock import patch, MagicMock

import src.tenant_onboarding as tenant_onboarding_module
from src.tenant_onboarding import onboard_new_tenant


class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")


def test_onboard_rejects_public_email():
    result = onboard_new_tenant("Hacker Inc", "hacker@gmail.com", "US")
    assert result["success"] is False
    assert "corporativo" in result["error"].lower() or "gmail" in result["error"].lower()


@patch("src.tenant_onboarding.requests.post")
@patch("src.tenant_onboarding.requests.get")
def test_onboard_creates_tenant(mock_get, mock_post, monkeypatch):
    monkeypatch.setenv("POCKETBASE_ADMIN_EMAIL", "admin@example.com")
    monkeypatch.setenv("POCKETBASE_ADMIN_PASSWORD", "secret")
    importlib.reload(tenant_onboarding_module)
    # Primer post: auth, segundo post: create tenant
    mock_post.side_effect = [
        MockResponse({"token": "admin-token"}),
        MockResponse({"id": "tenant-xyz"}),
    ]
    mock_get.return_value = MockResponse({"items": [], "totalPages": 1})

    result = tenant_onboarding_module.onboard_new_tenant("Delta Airlines", "admin@delta.com", "US")
    assert result["success"] is True, result
    assert result["data"]["tenant_id"] == "tenant-xyz"
    assert "live_key" in result["data"]
    assert "test_key" in result["data"]
