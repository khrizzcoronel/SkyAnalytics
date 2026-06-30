"""
Chaos engineering experiment runner with kill switch.

Simulates failure injection in staging and records recovery metrics.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum


class ExperimentStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    ABORTED = "aborted"
    PASSED = "passed"
    FAILED = "failed"


@dataclass
class ChaosExperiment:
    experiment_id: str
    namespace: str
    fault_type: str  # pod_delete, network_latency, db_failover, etc.
    target_pods_pct: float
    status: ExperimentStatus = ExperimentStatus.PENDING
    started_at: Optional[datetime] = None
    recovered_at: Optional[datetime] = None
    alerts_fired: List[str] = field(default_factory=list)


class ChaosEngineeringRunner:
    """Run chaos experiments with emergency abort capability."""

    def __init__(self):
        self._experiments: Dict[str, ChaosExperiment] = {}
        self._abort_flags: Dict[str, bool] = {}

    def start(self, experiment: ChaosExperiment) -> None:
        if experiment.namespace.lower() == "production":
            raise ValueError("Chaos experiments are not allowed in production")
        experiment.status = ExperimentStatus.RUNNING
        experiment.started_at = datetime.utcnow()
        self._experiments[experiment.experiment_id] = experiment
        self._abort_flags[experiment.experiment_id] = False

    def abort(self, experiment_id: str) -> bool:
        experiment = self._experiments.get(experiment_id)
        if not experiment:
            return False
        self._abort_flags[experiment_id] = True
        experiment.status = ExperimentStatus.ABORTED
        return True

    def record_recovery(self, experiment_id: str) -> Optional[ChaosExperiment]:
        experiment = self._experiments.get(experiment_id)
        if not experiment or experiment.status != ExperimentStatus.RUNNING:
            return None
        if self._abort_flags.get(experiment_id):
            experiment.status = ExperimentStatus.ABORTED
            return experiment
        experiment.recovered_at = datetime.utcnow()
        experiment.status = ExperimentStatus.PASSED
        return experiment

    def record_alert(self, experiment_id: str, alert: str) -> None:
        experiment = self._experiments.get(experiment_id)
        if experiment:
            experiment.alerts_fired.append(alert)

    def mttr_seconds(self, experiment_id: str) -> Optional[float]:
        experiment = self._experiments.get(experiment_id)
        if not experiment or not experiment.started_at or not experiment.recovered_at:
            return None
        return (experiment.recovered_at - experiment.started_at).total_seconds()
