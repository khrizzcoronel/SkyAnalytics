"""
Load test result analyzer.

Evaluates k6-style load test metrics against resilience SLOs.
"""
from dataclasses import dataclass
from typing import Dict


@dataclass
class LoadTestResult:
    vus: int
    requests_per_second: float
    http_error_rate_pct: float
    p95_latency_ms: float
    p99_latency_ms: float


class LoadTestAnalyzer:
    """Check if a load test result meets the SLOs."""

    P95_LATENCY_THRESHOLD_MS = 500.0
    MAX_ERROR_RATE_PCT = 1.0

    def evaluate(self, result: LoadTestResult) -> Dict:
        p95_ok = result.p95_latency_ms <= self.P95_LATENCY_THRESHOLD_MS
        errors_ok = result.http_error_rate_pct <= self.MAX_ERROR_RATE_PCT
        passed = p95_ok and errors_ok
        return {
            "passed": passed,
            "vus": result.vus,
            "rps": result.requests_per_second,
            "p95_latency_ms": result.p95_latency_ms,
            "p99_latency_ms": result.p99_latency_ms,
            "http_error_rate_pct": result.http_error_rate_pct,
            "checks": {
                "p95_under_500ms": p95_ok,
                "error_rate_under_1pct": errors_ok,
            },
        }
