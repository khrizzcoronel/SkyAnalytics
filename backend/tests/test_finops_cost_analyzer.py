from src.finops.cost_analyzer import CostAnalyzer, CostRecord


def test_detects_cost_spike_above_threshold():
    history = [
        {"AmazonS3": 100.0, "EC2": 200.0},
        {"AmazonS3": 110.0, "EC2": 190.0},
    ]
    analyzer = CostAnalyzer(history)
    today = {"AmazonS3": 150.0, "EC2": 195.0}
    alerts = analyzer.detect_spikes(today)
    assert any(alert.service == "AmazonS3" for alert in alerts)
    assert not any(alert.service == "EC2" for alert in alerts)


def test_tag_breakdown_groups_by_tag():
    records = [
        CostRecord(service="EC2", cost_usd=100.0, tags={"Environment": "Production"}),
        CostRecord(service="EC2", cost_usd=50.0, tags={"Environment": "Dev"}),
        CostRecord(service="S3", cost_usd=30.0, tags={"Environment": "Production"}),
    ]
    analyzer = CostAnalyzer([])
    breakdown = analyzer.tag_breakdown(records, "Environment")
    assert breakdown["Production"] == 130.0
    assert breakdown["Dev"] == 50.0


def test_find_zombies_identifies_unattached_and_idle():
    resources = [
        {"id": "vol-1", "type": "EBS", "unattached": True, "monthly_cost": 10.0},
        {"id": "ip-1", "type": "EIP", "idle_days": 10, "monthly_cost": 3.6},
        {"id": "ec2-1", "type": "EC2", "idle_days": 2, "monthly_cost": 50.0},
    ]
    analyzer = CostAnalyzer([])
    zombies = analyzer.find_zombies(resources)
    assert len(zombies) == 2
    ids = {z.resource_id for z in zombies}
    assert "vol-1" in ids
    assert "ip-1" in ids
