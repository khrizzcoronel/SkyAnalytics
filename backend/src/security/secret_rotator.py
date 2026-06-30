import secrets
import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Optional


class SecretStore(ABC):
    """Abstract store for secrets. Production impl puede usar AWS Secrets Manager / Vault."""

    @abstractmethod
    def get_secret_metadata(self, secret_name: str) -> dict:
        """Retorna dict con 'value', 'created_at' (iso), 'rotated_at' (iso)."""
        ...

    @abstractmethod
    def put_secret(self, secret_name: str, value: str) -> None:
        ...


class InMemorySecretStore(SecretStore):
    def __init__(self, secrets: Optional[dict] = None):
        self._secrets = secrets or {}

    def get_secret_metadata(self, secret_name: str) -> dict:
        return self._secrets.get(secret_name, {})

    def put_secret(self, secret_name: str, value: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        meta = self._secrets.get(secret_name, {})
        self._secrets[secret_name] = {
            "value": value,
            "created_at": meta.get("created_at", now),
            "rotated_at": now,
        }


@dataclass
class RotationResult:
    secret_name: str
    rotated: bool
    previous_age_days: int
    new_value: Optional[str] = None
    overlap_until: Optional[datetime] = None
    message: str = ""


class SecretRotator:
    """
    Rota secretos cuando superan `max_age_days`.
    Soporta periodo de overlap donde el secreto anterior sigue válido.
    """

    def __init__(
        self,
        store: SecretStore,
        max_age_days: int = 30,
        overlap_minutes: int = 5,
    ):
        self.store = store
        self.max_age_days = max_age_days
        self.overlap_minutes = overlap_minutes

    @staticmethod
    def _generate_password(length: int = 32) -> str:
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        return "".join(secrets.choice(alphabet) for _ in range(length))

    def _age_days(self, meta: dict) -> int:
        rotated_at = meta.get("rotated_at") or meta.get("created_at")
        if not rotated_at:
            return 0
        rotated = datetime.fromisoformat(rotated_at)
        if rotated.tzinfo is None:
            rotated = rotated.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - rotated).days

    def rotate_secret_if_needed(self, secret_name: str) -> RotationResult:
        meta = self.store.get_secret_metadata(secret_name)
        age_days = self._age_days(meta)

        if age_days <= self.max_age_days:
            return RotationResult(
                secret_name=secret_name,
                rotated=False,
                previous_age_days=age_days,
                message="Secret is still valid.",
            )

        new_pwd = self._generate_password()
        self.store.put_secret(secret_name, new_pwd)
        overlap_until = datetime.now(timezone.utc) + timedelta(minutes=self.overlap_minutes)

        return RotationResult(
            secret_name=secret_name,
            rotated=True,
            previous_age_days=age_days,
            new_value=new_pwd,
            overlap_until=overlap_until,
            message=(
                f"Secret rotated after {age_days} days. "
                f"Previous value remains valid until {overlap_until.isoformat()} (overlap period)."
            ),
        )


if __name__ == "__main__":
    store = InMemorySecretStore(
        {
            "DB_PASSWORD_PROD": {
                "value": "old-password",
                "created_at": (datetime.now(timezone.utc) - timedelta(days=45)).isoformat(),
            }
        }
    )
    rotator = SecretRotator(store)
    print(rotator.rotate_secret_if_needed("DB_PASSWORD_PROD"))
    print(rotator.rotate_secret_if_needed("STRIPE_API_KEY"))
