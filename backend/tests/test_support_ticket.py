from datetime import datetime, timedelta

from src.support.ticket_service import TicketService, SupportTicket, Plan, Severity


def test_enterprise_critical_ticket_gets_s1():
    svc = TicketService()
    ticket = SupportTicket(
        ticket_id="T-001",
        tenant_id="tenant-42",
        plan=Plan.ENTERPRISE,
        title="API outage",
        description="Endpoint returns 500 for all requests",
    )
    svc.triage(ticket)
    assert ticket.severity == Severity.S1


def test_freemium_ticket_gets_lowest_severity():
    svc = TicketService()
    ticket = SupportTicket(
        ticket_id="T-002",
        tenant_id="tenant-7",
        plan=Plan.FREEMIUM,
        title="API outage",
        description="Endpoint returns 500",
    )
    svc.triage(ticket)
    assert ticket.severity == Severity.S4


def test_cannot_escalate_without_reproduction_steps():
    svc = TicketService()
    ticket = SupportTicket(
        ticket_id="T-003",
        tenant_id="tenant-42",
        plan=Plan.ENTERPRISE,
        title="Bug",
        description="Something broke",
    )
    assert not svc.can_move_to_engineering(ticket)


def test_can_resolve_only_with_linked_pr():
    svc = TicketService()
    ticket = SupportTicket(
        ticket_id="T-004",
        tenant_id="tenant-42",
        plan=Plan.ENTERPRISE,
        title="Bug",
        description="Details",
        pr_url="https://github.com/org/repo/pull/1",
    )
    assert svc.can_resolve(ticket)


def test_s1_breaches_sla_after_four_hours():
    svc = TicketService()
    ticket = SupportTicket(
        ticket_id="T-005",
        tenant_id="tenant-42",
        plan=Plan.ENTERPRISE,
        title="Critical bug",
        description="500 error",
        severity=Severity.S1,
        created_at=datetime.utcnow() - timedelta(hours=5),
    )
    assert svc.is_sla_breached(ticket)
