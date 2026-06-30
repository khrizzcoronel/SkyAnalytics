"""
FinOps budget gate for CI/CD.

Decides whether an infrastructure change requires additional approval based on
its projected cost impact.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class BudgetGateResult:
    requires_approval: bool
    estimated_monthly_delta_usd: float
    current_monthly_budget_usd: float
    reason: str


class BudgetGate:
    """Approve or escalate infrastructure cost changes."""

    DEFAULT_APPROVAL_THRESHOLD_PCT = 10.0

    def __init__(
        self,
        monthly_budget_usd: float,
        approval_threshold_pct: float = DEFAULT_APPROVAL_THRESHOLD_PCT,
    ):
        self.monthly_budget_usd = monthly_budget_usd
        self.approval_threshold_pct = approval_threshold_pct

    def evaluate(self, estimated_monthly_delta_usd: float) -> BudgetGateResult:
        threshold_usd = self.monthly_budget_usd * (self.approval_threshold_pct / 100)
        requires = estimated_monthly_delta_usd > threshold_usd
        reason = (
            f"Cost increase ${estimated_monthly_delta_usd:.2f} exceeds "
            f"{self.approval_threshold_pct}% of monthly budget (${threshold_usd:.2f})"
            if requires
            else "Cost increase within budget threshold"
        )
        return BudgetGateResult(
            requires_approval=requires,
            estimated_monthly_delta_usd=estimated_monthly_delta_usd,
            current_monthly_budget_usd=self.monthly_budget_usd,
            reason=reason,
        )
