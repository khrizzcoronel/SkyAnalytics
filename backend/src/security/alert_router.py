"""
Security alert router and auto-remediation.

Classifies incoming security events, routes them to the appropriate channel,
and applies automated Level-1 responses such as IP blocks.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional, Set


class Severity(Enum):
    SEV1 = "Sev1"
    SEV2 = "Sev2"
    SEV3 = "Sev3"


class Action(Enum):
    PAGE = "page"
    SLACK_SECURITY = "slack_security"
    BLOCK_IP = "block_ip"
    AUDIT_LOG = "audit_log"


@dataclass
class SecurityEvent:
    event_type: str
    source_ip: Optional[str]
    details: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Alert:
    severity: Severity
    message: str
    actions: List[Action] = field(default_factory=list)
    blocked_ip: Optional[str] = None


class AlertRouter:
    """Route security events and apply auto-remediation rules."""

    WHITELISTED_IPS: Set[str] = set()
    AUTO_BLOCK_EVENTS = {"brute_force", "port_scan"}
    SEV1_EVENTS = {"data_exfiltration", "crypto_mining", "root_compromise"}
    SEV2_EVENTS = {"port_scan", "tls_downgrade", "mass_failed_login"}

    def __init__(self, whitelisted_ips: Optional[Set[str]] = None):
        self.blocked_ips: Set[str] = set()
        self.whitelisted_ips = whitelisted_ips or set(self.WHITELISTED_IPS)

    def handle(self, event: SecurityEvent) -> Alert:
        severity = self._classify(event)
        actions: List[Action] = [Action.AUDIT_LOG]

        if severity == Severity.SEV1:
            actions.append(Action.PAGE)
        elif severity == Severity.SEV2:
            actions.append(Action.SLACK_SECURITY)
        else:
            actions.append(Action.SLACK_SECURITY)

        blocked_ip = None
        if (
            event.event_type in self.AUTO_BLOCK_EVENTS
            and event.source_ip
            and event.source_ip not in self.whitelisted_ips
        ):
            self.blocked_ips.add(event.source_ip)
            actions.append(Action.BLOCK_IP)
            blocked_ip = event.source_ip

        return Alert(
            severity=severity,
            message=f"{severity.value}: {event.event_type} - {event.details}",
            actions=actions,
            blocked_ip=blocked_ip,
        )

    def _classify(self, event: SecurityEvent) -> Severity:
        if event.event_type in self.SEV1_EVENTS:
            return Severity.SEV1
        if event.event_type in self.SEV2_EVENTS:
            return Severity.SEV2
        return Severity.SEV3

    def unblock(self, ip: str) -> bool:
        if ip in self.blocked_ips:
            self.blocked_ips.remove(ip)
            return True
        return False
