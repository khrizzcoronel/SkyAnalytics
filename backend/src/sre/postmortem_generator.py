"""
Post-mortem generator for SRE incident management.

Creates a blameless post-mortem template and validates that action items
are created before the post-mortem can be closed.
"""
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class Severity(Enum):
    SEV1 = "Sev1"
    SEV2 = "Sev2"
    SEV3 = "Sev3"


@dataclass
class ActionItem:
    title: str
    assignee: str
    priority: str = "P1"


@dataclass
class PostMortem:
    incident_id: str
    severity: Severity
    title: str
    summary: str = ""
    timeline: List[str] = field(default_factory=list)
    root_cause: str = ""
    action_items: List[ActionItem] = field(default_factory=list)
    approved_by: Optional[str] = None
    closed_at: Optional[datetime] = None

    def add_action_item(self, title: str, assignee: str, priority: str = "P1") -> None:
        self.action_items.append(ActionItem(title=title, assignee=assignee, priority=priority))

    def can_close(self, approver: Optional[str] = None) -> bool:
        """Sev1 incidents require an approver and at least one action item."""
        if self.severity == Severity.SEV1:
            if not approver and not self.approved_by:
                return False
            if not self.action_items:
                return False
        return True

    def close(self, approver: Optional[str] = None) -> None:
        if not self.can_close(approver):
            raise ValueError("Post-mortem cannot be closed without approver and action items")
        if approver:
            self.approved_by = approver
        self.closed_at = datetime.utcnow()

    def to_markdown(self) -> str:
        lines = [
            f"# Post-Mortem: {self.title}",
            "",
            f"- **Incident ID:** {self.incident_id}",
            f"- **Severity:** {self.severity.value}",
            f"- **Status:** {'Closed' if self.closed_at else 'Open'}",
            "",
            "## Summary",
            self.summary or "_Pending_",
            "",
            "## Timeline",
        ]
        lines.extend(f"- {event}" for event in self.timeline) or lines.append("_Pending_")
        lines.extend(["", "## Root Cause (5 Whys)", self.root_cause or "_Pending_", ""])
        lines.append("## Action Items")
        if self.action_items:
            for item in self.action_items:
                lines.append(f"- **[{item.priority}]** {item.title} — @{item.assignee}")
        else:
            lines.append("_None yet_")
        lines.append("")
        if self.approved_by:
            lines.append(f"Approved by: {self.approved_by}")
        return "\n".join(lines)


class PostMortemGenerator:
    """Generate blameless post-mortem documents."""

    def create(
        self,
        incident_id: str,
        severity: Severity,
        title: str,
        timeline: Optional[List[str]] = None,
    ) -> PostMortem:
        return PostMortem(
            incident_id=incident_id,
            severity=severity,
            title=title,
            timeline=timeline or [],
        )
