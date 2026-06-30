import pytest

from src.sre.postmortem_generator import PostMortemGenerator, Severity


def test_sev1_cannot_close_without_action_items_and_approver():
    gen = PostMortemGenerator()
    pm = gen.create(
        incident_id="INC-001",
        severity=Severity.SEV1,
        title="Database outage",
        timeline=["12:00 Issue detected", "12:20 Service restored"],
    )
    assert not pm.can_close()
    with pytest.raises(ValueError):
        pm.close()


def test_sev1_can_close_with_action_items_and_approver():
    gen = PostMortemGenerator()
    pm = gen.create(
        incident_id="INC-002",
        severity=Severity.SEV1,
        title="API latency spike",
    )
    pm.root_cause = "Missing timeout in migration script"
    pm.add_action_item("Add default timeouts to migrations", "sre-oncall")
    assert pm.can_close(approver="tech-lead")
    pm.close(approver="tech-lead")
    assert pm.closed_at is not None
    assert pm.approved_by == "tech-lead"


def test_markdown_contains_blameless_fields():
    gen = PostMortemGenerator()
    pm = gen.create(
        incident_id="INC-003",
        severity=Severity.SEV2,
        title="Cache degradation",
    )
    pm.root_cause = "Redis memory pressure"
    md = pm.to_markdown()
    assert "INC-003" in md
    assert "Cache degradation" in md
    assert "Redis memory pressure" in md
    assert "Approved by" not in md
