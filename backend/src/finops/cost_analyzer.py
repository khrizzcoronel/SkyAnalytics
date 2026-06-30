"""
FinOps cost analyzer.

Analyzes cloud billing data, detects cost spikes vs forecast, and identifies
zombie resources.
"""
from dataclasses import dataclass, field
from typing import List, Dict
from statistics import mean


@dataclass
class CostRecord:
    service: str
    cost_usd: float
    tags: Dict[str, str] = field(default_factory=dict)


@dataclass
class CostAlert:
    service: str
    actual: float
    forecast: float
    deviation_pct: float


@dataclass
class ZombieResource:
    resource_id: str
    resource_type: str
    reason: str
    estimated_monthly_cost: float


class CostAnalyzer:
    """Detect cost anomalies and unused resources."""

    SPIKE_THRESHOLD_PCT = 20.0
    ABSOLUTE_VARIANCE_USD = 100.0

    def __init__(self, daily_history: List[Dict[str, float]]):
        """
        daily_history: list of dicts mapping service -> cost for prior days.
        """
        self.daily_history = daily_history

    def forecast(self, service: str) -> float:
        """Simple rolling average forecast."""
        values = [day.get(service, 0.0) for day in self.daily_history]
        if not values:
            return 0.0
        return mean(values)

    def detect_spikes(self, today: Dict[str, float]) -> List[CostAlert]:
        alerts = []
        for service, actual in today.items():
            forecast = self.forecast(service)
            if forecast == 0:
                continue
            deviation_pct = ((actual - forecast) / forecast) * 100
            if deviation_pct > self.SPIKE_THRESHOLD_PCT or (
                actual - forecast > self.ABSOLUTE_VARIANCE_USD
                and deviation_pct > 0
            ):
                alerts.append(
                    CostAlert(
                        service=service,
                        actual=actual,
                        forecast=forecast,
                        deviation_pct=round(deviation_pct, 2),
                    )
                )
        return alerts

    def tag_breakdown(
        self,
        records: List[CostRecord],
        tag_key: str,
    ) -> Dict[str, float]:
        breakdown: Dict[str, float] = {}
        for record in records:
            tag_value = record.tags.get(tag_key, "untagged")
            breakdown[tag_value] = breakdown.get(tag_value, 0.0) + record.cost_usd
        return breakdown

    def find_zombies(
        self,
        resources: List[Dict],
    ) -> List[ZombieResource]:
        zombies = []
        for resource in resources:
            if resource.get("unattached"):
                zombies.append(
                    ZombieResource(
                        resource_id=resource["id"],
                        resource_type=resource["type"],
                        reason="Unattached volume",
                        estimated_monthly_cost=resource.get("monthly_cost", 0.0),
                    )
                )
            elif resource.get("idle_days", 0) > 7:
                zombies.append(
                    ZombieResource(
                        resource_id=resource["id"],
                        resource_type=resource["type"],
                        reason="Idle for more than 7 days",
                        estimated_monthly_cost=resource.get("monthly_cost", 0.0),
                    )
                )
        return zombies
