"""
FinOps snooze scheduler.

Decides which non-production resources can be safely stopped and restarted
based on tags.
"""
from dataclasses import dataclass, field
from typing import List
from enum import Enum


class Action(Enum):
    STOP = "stop"
    START = "start"
    SKIP = "skip"


@dataclass
class Resource:
    resource_id: str
    resource_type: str
    environment: str
    snooze_enabled: bool = True


@dataclass
class SnoozePlan:
    action: Action
    resource_id: str
    reason: str


class SnoozeScheduler:
    """Schedule weekend snoozing for dev resources."""

    def plan(self, resources: List[Resource], action: Action) -> List[SnoozePlan]:
        plans = []
        for resource in resources:
            if resource.environment.lower() == "production":
                plans.append(
                    SnoozePlan(
                        action=Action.SKIP,
                        resource_id=resource.resource_id,
                        reason="Production resources are never snoozed",
                    )
                )
            elif not resource.snooze_enabled:
                plans.append(
                    SnoozePlan(
                        action=Action.SKIP,
                        resource_id=resource.resource_id,
                        reason="FinOps-Snooze=False exemption",
                    )
                )
            else:
                plans.append(
                    SnoozePlan(
                        action=action,
                        resource_id=resource.resource_id,
                        reason=f"{action.value.capitalize()} dev resource",
                    )
                )
        return plans
