from src.finops.budget_gate import BudgetGate


def test_small_increase_does_not_require_approval():
    gate = BudgetGate(monthly_budget_usd=10_000)
    result = gate.evaluate(500)
    assert not result.requires_approval


def test_large_increase_requires_approval():
    gate = BudgetGate(monthly_budget_usd=10_000)
    result = gate.evaluate(1_500)
    assert result.requires_approval
    assert "exceeds" in result.reason
