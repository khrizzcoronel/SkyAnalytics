"""
OKR tracker with immutable audit log.

Validates OKR structure, prevents retroactive edits once closed, and
records every change.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum


class OkrStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    CLOSED = "closed"


@dataclass
class KeyResult:
    description: str
    target_value: float
    current_value: float = 0.0


@dataclass
class Objective:
    objective_id: str
    title: str
    assignee: str
    key_results: List[KeyResult]
    status: OkrStatus = OkrStatus.DRAFT


@dataclass
class AuditEvent:
    timestamp: datetime
    author: str
    action: str
    objective_id: str
    before: Optional[dict]
    after: Optional[dict]


class OkrTracker:
    """Track OKRs and enforce business rules."""

    MIN_KEY_RESULTS = 1
    MAX_KEY_RESULTS = 5

    def __init__(self):
        self._objectives: Dict[str, Objective] = {}
        self._audit_log: List[AuditEvent] = []

    def create(
        self,
        objective: Objective,
        author: str,
    ) -> Objective:
        if not self.MIN_KEY_RESULTS <= len(objective.key_results) <= self.MAX_KEY_RESULTS:
            raise ValueError(
                f"Objective must have between {self.MIN_KEY_RESULTS} and {self.MAX_KEY_RESULTS} key results"
            )
        self._objectives[objective.objective_id] = objective
        self._log(author, "create", objective.objective_id, None, {"title": objective.title})
        return objective

    def publish(self, objective_id: str, author: str) -> Objective:
        objective = self._get(objective_id)
        if objective.status == OkrStatus.CLOSED:
            raise ValueError("Cannot publish a closed objective")
        before = {"status": objective.status.value}
        objective.status = OkrStatus.ACTIVE
        self._log(author, "publish", objective_id, before, {"status": objective.status.value})
        return objective

    def close(self, objective_id: str, author: str) -> Objective:
        objective = self._get(objective_id)
        before = {"status": objective.status.value}
        objective.status = OkrStatus.CLOSED
        self._log(author, "close", objective_id, before, {"status": objective.status.value})
        return objective

    def update_key_result(
        self,
        objective_id: str,
        kr_index: int,
        current_value: float,
        author: str,
    ) -> Objective:
        objective = self._get(objective_id)
        if objective.status == OkrStatus.CLOSED:
            raise ValueError("Cannot modify a closed objective")
        kr = objective.key_results[kr_index]
        before = {"current_value": kr.current_value}
        kr.current_value = current_value
        self._log(
            author,
            "update_kr",
            objective_id,
            before,
            {"current_value": current_value, "kr_index": kr_index},
        )
        return objective

    def achievement_pct(self, objective_id: str) -> float:
        objective = self._get(objective_id)
        if not objective.key_results:
            return 0.0
        total = sum(
            min(100.0, (kr.current_value / kr.target_value) * 100)
            for kr in objective.key_results
            if kr.target_value
        )
        return total / len(objective.key_results)

    def audit_log(self) -> List[AuditEvent]:
        return list(self._audit_log)

    def _get(self, objective_id: str) -> Objective:
        if objective_id not in self._objectives:
            raise KeyError(f"Objective {objective_id} not found")
        return self._objectives[objective_id]

    def _log(
        self,
        author: str,
        action: str,
        objective_id: str,
        before: Optional[dict],
        after: Optional[dict],
    ) -> None:
        self._audit_log.append(
            AuditEvent(
                timestamp=datetime.utcnow(),
                author=author,
                action=action,
                objective_id=objective_id,
                before=before,
                after=after,
            )
        )
