"""
Sandbox token bucket rate limiter.

Enforces a strict per-token rate limit for the Developer Portal sandbox
calls without requiring a real corporate API key.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict


@dataclass
class TokenBucket:
    tokens: float
    last_refill: datetime


class SandboxRateLimiter:
    """In-memory token bucket rate limiter for sandbox requests."""

    def __init__(self, max_requests_per_minute: int = 10):
        self.max_requests = max_requests_per_minute
        self._buckets: Dict[str, TokenBucket] = {}

    def allow_request(self, token: str) -> bool:
        now = datetime.utcnow()
        bucket = self._buckets.get(token)
        if bucket is None:
            bucket = TokenBucket(tokens=float(self.max_requests), last_refill=now)
            self._buckets[token] = bucket

        # Refill tokens based on elapsed time since last request
        elapsed_minutes = (now - bucket.last_refill).total_seconds() / 60.0
        refill = elapsed_minutes * self.max_requests
        if refill > 0:
            bucket.tokens = min(self.max_requests, bucket.tokens + refill)
            bucket.last_refill = now

        if bucket.tokens >= 1:
            bucket.tokens -= 1
            return True
        return False

    def reset(self, token: str) -> None:
        self._buckets.pop(token, None)
