"""
Error Budget service for SRE reliability.

Calculates consumed error budget from uptime telemetry and enforces
deployment freeze rules. Only production deployments are penalized;
non-production environments remain unrestricted.
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class EndpointMetric:
    name: str
    uptime_pct: float


@dataclass(frozen=True)
class ErrorBudgetReport:
    sla_pct: float
    total_budget_seconds: float
    consumed_seconds: float
    consumed_pct: float
    freeze_threshold_pct: float
    is_frozen: bool
    production_blocked: bool


class ErrorBudgetService:
    """
    Computes error budget consumption over a rolling 30-day window.

    For a 99.0% SLA the allowed downtime is 1% of a 30-day month:
    2,592,000 seconds * 0.01 = 25,920 seconds (432 minutes).
    """

    SECONDS_IN_MONTH = 30 * 24 * 60 * 60
    DEFAULT_FREEZE_THRESHOLD_PCT = 80.0
    HOTFIX_PREFIXES = ("hotfix/", "reliability/", "fix/")

    def __init__(
        self,
        sla_pct: float = 99.0,
        freeze_threshold_pct: float = DEFAULT_FREEZE_THRESHOLD_PCT,
    ):
        if not 0 < sla_pct < 100:
            raise ValueError("sla_pct must be between 0 and 100")
        self.sla_pct = sla_pct
        self.freeze_threshold_pct = freeze_threshold_pct
        self.total_budget_seconds = (100 - sla_pct) / 100 * self.SECONDS_IN_MONTH

    def calculate(
        self,
        global_uptime_pct: float,
        endpoints: Optional[List[EndpointMetric]] = None,
    ) -> ErrorBudgetReport:
        """Calculate consumed error budget from global uptime."""
        downtime_pct = max(0.0, 100.0 - global_uptime_pct)
        consumed_seconds = round((downtime_pct / 100.0) * self.SECONDS_IN_MONTH, 6)
        consumed_pct = round(
            (consumed_seconds / self.total_budget_seconds) * 100
            if self.total_budget_seconds > 0
            else 0.0,
            6,
        )
        is_frozen = consumed_pct >= self.freeze_threshold_pct

        return ErrorBudgetReport(
            sla_pct=self.sla_pct,
            total_budget_seconds=self.total_budget_seconds,
            consumed_seconds=consumed_seconds,
            consumed_pct=consumed_pct,
            freeze_threshold_pct=self.freeze_threshold_pct,
            is_frozen=is_frozen,
            production_blocked=is_frozen,
        )

    def can_deploy_to_production(
        self,
        report: ErrorBudgetReport,
        branch_name: str,
        hotfix_approved_by_sre_count: int = 0,
    ) -> bool:
        """
        Determine whether a deployment to production is allowed.

        Non-production environments are always allowed. During a freeze,
        only hotfix/reliability branches with dual SRE approval pass.
        """
        if not report.production_blocked:
            return True

        normalized = branch_name.lower()
        is_hotfix = any(normalized.startswith(prefix) for prefix in self.HOTFIX_PREFIXES)
        return is_hotfix and hotfix_approved_by_sre_count >= 2
