import pytest

from src.okr.okr_tracker import OkrTracker, Objective, KeyResult, OkrStatus


def test_create_objective_with_valid_key_results():
    tracker = OkrTracker()
    obj = Objective(
        objective_id="OKR-Q4-001",
        title="Reduce churn",
        assignee="VP Customer Success",
        key_results=[KeyResult("Churn under 0.5%", target_value=0.5)],
    )
    tracker.create(obj, author="founder")
    assert tracker.achievement_pct("OKR-Q4-001") == 0


def test_create_objective_with_too_many_key_results_fails():
    tracker = OkrTracker()
    obj = Objective(
        objective_id="OKR-Q4-002",
        title="Too many KRs",
        assignee="CTO",
        key_results=[KeyResult(f"KR{i}", target_value=1) for i in range(6)],
    )
    with pytest.raises(ValueError):
        tracker.create(obj, author="founder")


def test_closed_objective_cannot_be_modified():
    tracker = OkrTracker()
    obj = Objective(
        objective_id="OKR-Q4-003",
        title="ARR growth",
        assignee="CFO",
        key_results=[KeyResult("ARR $2M", target_value=2_000_000)],
    )
    tracker.create(obj, author="founder")
    tracker.publish("OKR-Q4-003", author="founder")
    tracker.close("OKR-Q4-003", author="founder")
    with pytest.raises(ValueError):
        tracker.update_key_result("OKR-Q4-003", 0, current_value=1_500_000, author="founder")


def test_audit_log_records_events():
    tracker = OkrTracker()
    obj = Objective(
        objective_id="OKR-Q4-004",
        title="NPS",
        assignee="CXO",
        key_results=[KeyResult("NPS > 50", target_value=50)],
    )
    tracker.create(obj, author="founder")
    tracker.publish("OKR-Q4-004", author="founder")
    log = tracker.audit_log()
    assert len(log) == 2
    assert log[0].action == "create"
    assert log[1].action == "publish"


def test_achievement_percentage_calculation():
    tracker = OkrTracker()
    obj = Objective(
        objective_id="OKR-Q4-005",
        title="Uptime",
        assignee="SRE Lead",
        key_results=[KeyResult("Uptime 99.9%", target_value=99.9, current_value=99.5)],
    )
    tracker.create(obj, author="founder")
    pct = tracker.achievement_pct("OKR-Q4-005")
    assert abs(pct - (99.5 / 99.9 * 100)) < 0.01
