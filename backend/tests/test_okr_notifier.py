from src.okr.slack_notifier import SlackNotifier
from src.okr.okr_tracker import OkrTracker, Objective, KeyResult


def test_slack_sink_receives_publish_notification():
    sink = []
    notifier = SlackNotifier(sink=sink)
    tracker = OkrTracker()
    obj = Objective(
        objective_id="OKR-Q4-006",
        title="Launch API v2",
        assignee="CTO",
        key_results=[KeyResult("100 Beta testers", target_value=100)],
    )
    tracker.create(obj, author="founder")
    tracker.publish("OKR-Q4-006", author="founder")

    summary = f"OKR published: {obj.title} — {obj.assignee}"
    notifier.send("#anuncios-globales", summary)

    assert len(sink) == 1
    assert sink[0].channel == "#anuncios-globales"
    assert "Launch API v2" in sink[0].text
