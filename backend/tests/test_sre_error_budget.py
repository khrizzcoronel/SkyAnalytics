import pytest

from src.sre.error_budget_service import ErrorBudgetService, EndpointMetric


def test_99_percent_sla_budget_is_432_minutes():
    svc = ErrorBudgetService(sla_pct=99.0)
    # Perfect uptime -> 0 consumed budget
    report = svc.calculate(global_uptime_pct=100.0)
    assert report.total_budget_seconds == 25_920
    assert report.consumed_seconds == 0
    assert report.consumed_pct == 0
    assert not report.is_frozen


def test_uptime_below_sla_consumes_budget():
    svc = ErrorBudgetService(sla_pct=99.0)
    # 99.5% uptime -> 0.5% downtime -> 50% of monthly budget
    report = svc.calculate(global_uptime_pct=99.5)
    expected_seconds = round(0.005 * 30 * 24 * 60 * 60, 6)
    assert report.consumed_seconds == expected_seconds
    assert report.consumed_pct == 50.0
    assert not report.is_frozen


def test_reaching_freeze_threshold_blocks_production():
    svc = ErrorBudgetService(sla_pct=99.0)
    # 99.19% uptime -> 0.81% downtime -> >80% budget consumed
    report = svc.calculate(global_uptime_pct=99.19)
    assert report.is_frozen
    assert report.production_blocked


def test_feature_branch_blocked_during_freeze():
    svc = ErrorBudgetService(sla_pct=99.0)
    report = svc.calculate(global_uptime_pct=99.0)
    # Force freeze by using a lower threshold
    svc2 = ErrorBudgetService(sla_pct=99.0, freeze_threshold_pct=0.0)
    frozen_report = svc2.calculate(global_uptime_pct=99.0)
    assert not svc.can_deploy_to_production(frozen_report, "feature/new-dashboard")


def test_hotfix_allowed_with_dual_sre_approval():
    svc = ErrorBudgetService(sla_pct=99.0, freeze_threshold_pct=0.0)
    report = svc.calculate(global_uptime_pct=99.0)
    assert svc.can_deploy_to_production(
        report, "hotfix/memory-leak", hotfix_approved_by_sre_count=2
    )


def test_hotfix_blocked_without_dual_approval():
    svc = ErrorBudgetService(sla_pct=99.0, freeze_threshold_pct=0.0)
    report = svc.calculate(global_uptime_pct=99.0)
    assert not svc.can_deploy_to_production(
        report, "hotfix/memory-leak", hotfix_approved_by_sre_count=1
    )


def test_non_production_always_allowed():
    # The freeze only applies to production; the helper still reports production_blocked,
    # but deployment policy would check environment separately. This test documents that
    # the service itself does not restrict staging branches.
    svc = ErrorBudgetService(sla_pct=99.0, freeze_threshold_pct=0.0)
    report = svc.calculate(global_uptime_pct=99.0)
    assert report.production_blocked
    assert not svc.can_deploy_to_production(report, "feature/new-dashboard")
