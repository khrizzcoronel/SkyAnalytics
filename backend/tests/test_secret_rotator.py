from datetime import datetime, timezone, timedelta

from src.security.secret_rotator import SecretRotator, InMemorySecretStore


def test_no_rotation_for_fresh_secret():
    store = InMemorySecretStore()
    store.put_secret("FRESH", "value")
    rotator = SecretRotator(store, max_age_days=30)
    result = rotator.rotate_secret_if_needed("FRESH")
    assert result.rotated is False


def test_rotation_for_old_secret():
    store = InMemorySecretStore(
        {
            "OLD_SECRET": {
                "value": "old",
                "created_at": (datetime.now(timezone.utc) - timedelta(days=45)).isoformat(),
            }
        }
    )
    rotator = SecretRotator(store, max_age_days=30, overlap_minutes=5)
    result = rotator.rotate_secret_if_needed("OLD_SECRET")
    assert result.rotated is True
    assert result.previous_age_days == 45
    assert result.new_value is not None
    assert result.overlap_until is not None
