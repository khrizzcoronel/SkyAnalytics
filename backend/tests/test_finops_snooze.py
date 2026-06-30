from src.finops.snooze_scheduler import SnoozeScheduler, Resource, Action


def test_dev_resources_are_stopped():
    scheduler = SnoozeScheduler()
    resources = [
        Resource(resource_id="dev-1", resource_type="EC2", environment="Dev"),
        Resource(resource_id="dev-2", resource_type="RDS", environment="dev"),
    ]
    plans = scheduler.plan(resources, Action.STOP)
    assert all(p.action == Action.STOP for p in plans)


def test_production_resources_never_snoozed():
    scheduler = SnoozeScheduler()
    resources = [
        Resource(resource_id="prod-1", resource_type="EC2", environment="Production"),
    ]
    plans = scheduler.plan(resources, Action.STOP)
    assert plans[0].action == Action.SKIP
    assert "Production" in plans[0].reason


def test_snooze_exemption_is_respected():
    scheduler = SnoozeScheduler()
    resources = [
        Resource(resource_id="dev-3", resource_type="EC2", environment="Dev", snooze_enabled=False),
    ]
    plans = scheduler.plan(resources, Action.STOP)
    assert plans[0].action == Action.SKIP
