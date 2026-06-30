"""
Sprint management service.

Tracks tickets across a sprint and enforces prioritization rules for
post-mortem/security action items.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional


class Priority(Enum):
    URGENT = "urgent"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class TicketStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    DONE = "done"


@dataclass
class SprintTicket:
    ticket_id: str
    title: str
    priority: Priority
    status: TicketStatus = TicketStatus.TODO
    story_points: int = 0
    okr_link: Optional[str] = None
    pr_merged: bool = False
    tests_passing: bool = False
    docs_updated: bool = False


@dataclass
class Sprint:
    sprint_id: str
    start_date: datetime
    end_date: datetime
    tickets: List[SprintTicket] = field(default_factory=list)

    def remaining_days(self) -> float:
        return max(0, (self.end_date - datetime.utcnow()).total_seconds() / 86400)


class SprintManager:
    """Manage sprint contents, status transitions and Definition of Done."""

    def __init__(self, sprint: Sprint):
        self.sprint = sprint

    def add_ticket(self, ticket: SprintTicket) -> None:
        self.sprint.tickets.append(ticket)
        self._sort_tickets()

    def _sort_tickets(self) -> None:
        priority_order = {
            Priority.URGENT: 0,
            Priority.HIGH: 1,
            Priority.MEDIUM: 2,
            Priority.LOW: 3,
        }
        self.sprint.tickets.sort(key=lambda t: priority_order[t.priority])

    def transition(
        self,
        ticket_id: str,
        new_status: TicketStatus,
    ) -> Optional[SprintTicket]:
        ticket = self._find(ticket_id)
        if not ticket:
            return None

        # Only auto-close via PR merge
        if new_status == TicketStatus.DONE and not ticket.pr_merged:
            return None

        ticket.status = new_status
        return ticket

    def definition_of_done_met(self, ticket: SprintTicket) -> bool:
        return ticket.pr_merged and ticket.tests_passing and ticket.docs_updated

    def burndown(self) -> dict:
        total_points = sum(t.story_points for t in self.sprint.tickets)
        done_points = sum(
            t.story_points
            for t in self.sprint.tickets
            if t.status == TicketStatus.DONE
        )
        return {
            "total_points": total_points,
            "done_points": done_points,
            "remaining_points": total_points - done_points,
            "completion_pct": (done_points / total_points * 100) if total_points else 0,
        }

    def reject_orphan_feature(self, ticket: SprintTicket) -> bool:
        """Feature tickets must be linked to an OKR."""
        if "feature" in ticket.title.lower() and not ticket.okr_link:
            return False
        return True

    def _find(self, ticket_id: str) -> Optional[SprintTicket]:
        for ticket in self.sprint.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None
