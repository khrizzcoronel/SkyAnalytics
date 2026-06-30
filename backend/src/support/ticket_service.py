"""
Customer support ticket service.

Handles triage, severity assignment and SLA rules for support tickets.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional


class Severity(Enum):
    S1 = "S1"  # Critical
    S2 = "S2"  # High
    S3 = "S3"  # Medium
    S4 = "S4"  # Low


class Plan(Enum):
    FREEMIUM = "freemium"
    PRO = "pro"
    ENTERPRISE = "enterprise"


@dataclass
class SupportTicket:
    ticket_id: str
    tenant_id: str
    plan: Plan
    title: str
    description: str
    reproduction_steps: Optional[str] = None
    severity: Optional[Severity] = None
    github_issue_url: Optional[str] = None
    pr_url: Optional[str] = None
    status: str = "open"
    created_at: datetime = field(default_factory=datetime.utcnow)
    resolved_at: Optional[datetime] = None


class TicketService:
    """Triage and manage support tickets."""

    SLA_TARGETS = {
        Plan.ENTERPRISE: {"first_response_minutes": 30, "critical_resolution_hours": 4},
        Plan.PRO: {"first_response_minutes": 4 * 60, "critical_resolution_hours": None},
        Plan.FREEMIUM: {"first_response_minutes": None, "critical_resolution_hours": None},
    }

    CRITICAL_KEYWORDS = {"outage", "down", "500", "critical", "sev1", "data loss"}
    HIGH_KEYWORDS = {"bug", "error", "slow", "latency", "sev2"}

    def triage(self, ticket: SupportTicket) -> SupportTicket:
        """Assign severity based on plan and keywords."""
        text = f"{ticket.title} {ticket.description}".lower()
        has_critical = any(kw in text for kw in self.CRITICAL_KEYWORDS)
        has_high = any(kw in text for kw in self.HIGH_KEYWORDS)

        if ticket.plan == Plan.ENTERPRISE and has_critical:
            ticket.severity = Severity.S1
        elif ticket.plan in (Plan.ENTERPRISE, Plan.PRO) and has_high:
            ticket.severity = Severity.S2
        elif ticket.plan == Plan.FREEMIUM:
            ticket.severity = Severity.S4
        else:
            ticket.severity = Severity.S3

        return ticket

    def can_move_to_engineering(self, ticket: SupportTicket) -> bool:
        """Require reproduction steps before escalating to engineering."""
        return bool(ticket.reproduction_steps and ticket.reproduction_steps.strip())

    def can_resolve(self, ticket: SupportTicket) -> bool:
        """Require a linked PR before resolving the ticket."""
        return bool(ticket.pr_url)

    def is_sla_breached(self, ticket: SupportTicket) -> bool:
        """Check if critical ticket resolution SLA is breached."""
        if ticket.severity != Severity.S1:
            return False
        if ticket.resolved_at:
            return False
        sla = self.SLA_TARGETS.get(ticket.plan, {})
        limit_hours = sla.get("critical_resolution_hours")
        if not limit_hours:
            return False
        return datetime.utcnow() - ticket.created_at > timedelta(hours=limit_hours)
