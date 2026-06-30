"""
OKR financial simulator.

Projects ARR based on new customers, churn rate, and CAC budget assumptions.
"""
from dataclasses import dataclass


@dataclass
class SimulationInputs:
    starting_arr: float
    avg_revenue_per_customer: float
    estimated_new_customers: int
    projected_churn_rate: float
    cac_budget: float


@dataclass
class SimulationResult:
    projected_arr: float
    new_revenue: float
    churned_revenue: float
    cac_per_customer: float
    feasible: bool
    warnings: list


class FinancialSimulator:
    """Run what-if scenarios for quarterly OKR planning."""

    def simulate(self, inputs: SimulationInputs) -> SimulationResult:
        warnings = []
        if inputs.projected_churn_rate < 0 or inputs.projected_churn_rate > 1:
            raise ValueError("Churn rate must be between 0 and 1")
        if inputs.estimated_new_customers < 0:
            raise ValueError("New customers cannot be negative")

        new_revenue = inputs.estimated_new_customers * inputs.avg_revenue_per_customer
        churned_revenue = inputs.starting_arr * inputs.projected_churn_rate
        projected_arr = inputs.starting_arr + new_revenue - churned_revenue

        cac_per_customer = (
            inputs.cac_budget / inputs.estimated_new_customers
            if inputs.estimated_new_customers > 0
            else 0.0
        )

        feasible = True
        if cac_per_customer > inputs.avg_revenue_per_customer * 0.5:
            warnings.append("CAC exceeds 50% of first-year ARR")
            feasible = False

        return SimulationResult(
            projected_arr=round(projected_arr, 2),
            new_revenue=round(new_revenue, 2),
            churned_revenue=round(churned_revenue, 2),
            cac_per_customer=round(cac_per_customer, 2),
            feasible=feasible,
            warnings=warnings,
        )
