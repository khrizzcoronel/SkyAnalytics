import pytest

from src.okr.financial_simulator import FinancialSimulator, SimulationInputs


def test_simulation_projects_arr():
    sim = FinancialSimulator()
    inputs = SimulationInputs(
        starting_arr=1_000_000,
        avg_revenue_per_customer=10_000,
        estimated_new_customers=50,
        projected_churn_rate=0.02,
        cac_budget=200_000,
    )
    result = sim.simulate(inputs)
    assert result.projected_arr == 1_000_000 + 500_000 - 20_000
    assert result.feasible


def test_negative_churn_rate_is_rejected():
    sim = FinancialSimulator()
    inputs = SimulationInputs(
        starting_arr=1_000_000,
        avg_revenue_per_customer=10_000,
        estimated_new_customers=50,
        projected_churn_rate=-0.01,
        cac_budget=200_000,
    )
    with pytest.raises(ValueError):
        sim.simulate(inputs)


def test_high_cac_generates_warning():
    sim = FinancialSimulator()
    inputs = SimulationInputs(
        starting_arr=1_000_000,
        avg_revenue_per_customer=10_000,
        estimated_new_customers=10,
        projected_churn_rate=0.02,
        cac_budget=100_000,
    )
    result = sim.simulate(inputs)
    assert not result.feasible
    assert any("CAC" in w for w in result.warnings)
