"""
Terraform state lock simulator.

Prevents concurrent Terraform applies by enforcing a distributed lock.
A DynamoDB-backed adapter can be implemented later.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional
from threading import Lock


@dataclass
class LockInfo:
    lock_id: str
    owner: str
    acquired_at: datetime
    expires_at: datetime


class TerraformStateLock:
    """In-memory Terraform state lock with TTL."""

    def __init__(self, ttl_seconds: int = 600):
        self._ttl = timedelta(seconds=ttl_seconds)
        self._lock: Optional[LockInfo] = None
        self._mutex = Lock()

    def acquire(self, owner: str) -> Optional[LockInfo]:
        with self._mutex:
            now = datetime.utcnow()
            if self._lock and self._lock.expires_at > now:
                return None
            info = LockInfo(
                lock_id=f"lock-{now.isoformat()}",
                owner=owner,
                acquired_at=now,
                expires_at=now + self._ttl,
            )
            self._lock = info
            return info

    def release(self, owner: str) -> bool:
        with self._mutex:
            if self._lock and self._lock.owner == owner:
                self._lock = None
                return True
            return False

    def is_locked(self) -> bool:
        with self._mutex:
            if not self._lock:
                return False
            return self._lock.expires_at > datetime.utcnow()
