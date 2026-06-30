from datetime import datetime, timedelta

from src.resilience.chaos_engineering import ChaosEngineeringRunner, ChaosExperiment, ExperimentStatus


def test_cannot_run_chaos_in_production():
    runner = ChaosEngineeringRunner()
    experiment = ChaosExperiment(
        experiment_id="exp-1",
        namespace="production",
        fault_type="pod_delete",
        target_pods_pct=30,
    )
    try:
        runner.start(experiment)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "production" in str(e).lower()


def test_experiment_lifecycle_and_mttr():
    runner = ChaosEngineeringRunner()
    experiment = ChaosExperiment(
        experiment_id="exp-2",
        namespace="staging",
        fault_type="db_failover",
        target_pods_pct=50,
    )
    runner.start(experiment)
    runner.record_alert("exp-2", "master-db-down")
    runner.record_recovery("exp-2")
    assert experiment.status == ExperimentStatus.PASSED
    assert "master-db-down" in experiment.alerts_fired
    mttr = runner.mttr_seconds("exp-2")
    assert mttr is not None
    assert mttr >= 0


def test_kill_switch_aborts_experiment():
    runner = ChaosEngineeringRunner()
    experiment = ChaosExperiment(
        experiment_id="exp-3",
        namespace="staging",
        fault_type="network_latency",
        target_pods_pct=20,
    )
    runner.start(experiment)
    assert runner.abort("exp-3")
    runner.record_recovery("exp-3")
    assert experiment.status == ExperimentStatus.ABORTED
