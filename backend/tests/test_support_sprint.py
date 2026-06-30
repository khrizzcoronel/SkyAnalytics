from datetime import datetime, timedelta

from src.support.sprint_manager import SprintManager, Sprint, SprintTicket, Priority, TicketStatus


def test_urgent_tickets_sorted_to_top():
    sprint = Sprint(
        sprint_id="S1",
        start_date=datetime.utcnow(),
        end_date=datetime.utcnow() + timedelta(days=14),
    )
    manager = SprintManager(sprint)
    manager.add_ticket(SprintTicket(ticket_id="LOW-1", title="Docs", priority=Priority.LOW))
    manager.add_ticket(SprintTicket(ticket_id="URG-1", title="Post-mortem action", priority=Priority.URGENT))
    assert sprint.tickets[0].ticket_id == "URG-1"


def test_feature_ticket_rejected_without_okr():
    sprint = Sprint(sprint_id="S1", start_date=datetime.utcnow(), end_date=datetime.utcnow() + timedelta(days=14))
    manager = SprintManager(sprint)
    feature = SprintTicket(ticket_id="FEAT-1", title="Feature: new dashboard", priority=Priority.MEDIUM)
    assert not manager.reject_orphan_feature(feature)


def test_done_transition_requires_merged_pr():
    sprint = Sprint(sprint_id="S1", start_date=datetime.utcnow(), end_date=datetime.utcnow() + timedelta(days=14))
    manager = SprintManager(sprint)
    ticket = SprintTicket(ticket_id="BUG-1", title="Bug fix", priority=Priority.HIGH)
    manager.add_ticket(ticket)
    result = manager.transition("BUG-1", TicketStatus.DONE)
    assert result is None

    ticket.pr_merged = True
    ticket.tests_passing = True
    ticket.docs_updated = True
    result = manager.transition("BUG-1", TicketStatus.DONE)
    assert result is not None
    assert result.status == TicketStatus.DONE


def test_burndown_calculation():
    sprint = Sprint(sprint_id="S1", start_date=datetime.utcnow(), end_date=datetime.utcnow() + timedelta(days=14))
    manager = SprintManager(sprint)
    manager.add_ticket(SprintTicket(ticket_id="T1", title="A", priority=Priority.HIGH, story_points=5))
    manager.add_ticket(SprintTicket(ticket_id="T2", title="B", priority=Priority.LOW, story_points=3, status=TicketStatus.DONE, pr_merged=True, tests_passing=True, docs_updated=True))
    burndown = manager.burndown()
    assert burndown["total_points"] == 8
    assert burndown["done_points"] == 3
    assert burndown["remaining_points"] == 5
