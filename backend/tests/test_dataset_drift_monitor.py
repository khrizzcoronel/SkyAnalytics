import numpy as np
from src.quality.dataset_drift_monitor import calculate_psi


def test_calculate_psi_stable():
    np.random.seed(42)
    expected = np.random.normal(10, 2, 1000)
    actual = np.random.normal(10, 2, 200)
    psi = calculate_psi(expected, actual)
    assert psi < 0.1


def test_calculate_psi_critical():
    np.random.seed(42)
    expected = np.random.normal(10, 2, 1000)
    actual = np.random.normal(25, 5, 200)
    psi = calculate_psi(expected, actual)
    assert psi > 0.25
