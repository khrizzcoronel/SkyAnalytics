"""
RapidAPI marketplace gateway validator and rate limiter.

Validates proxy-secret headers and enforces per-plan monthly hard limits.
"""
from dataclasses import dataclass
from typing import Dict
from enum import Enum


class RapidPlan(Enum):
    FREEMIUM = "freemium"
    PRO = "pro"
    ULTRA = "ultra"


@dataclass
class RapidApiRequest:
    proxy_secret: str
    user: str
    plan: RapidPlan


class RapidApiGateway:
    """Authenticate and rate-limit RapidAPI requests."""

    PLAN_LIMITS = {
        RapidPlan.FREEMIUM: 1_000,
        RapidPlan.PRO: 10_000,
        RapidPlan.ULTRA: 100_000,
    }

    def __init__(self, expected_secret: str):
        self.expected_secret = expected_secret
        self.usage: Dict[str, int] = {}

    def authenticate(self, request: RapidApiRequest) -> bool:
        return request.proxy_secret == self.expected_secret

    def allow_request(self, request: RapidApiRequest) -> bool:
        if not self.authenticate(request):
            return False
        limit = self.PLAN_LIMITS[request.plan]
        current = self.usage.get(request.user, 0)
        if current >= limit:
            return False
        self.usage[request.user] = current + 1
        return True

    def reset(self, user: str) -> None:
        self.usage.pop(user, None)
