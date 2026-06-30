from src.resilience.load_test_analyzer import LoadTestAnalyzer, LoadTestResult


def test_load_test_passes_when_slo_met():
    analyzer = LoadTestAnalyzer()
    result = LoadTestResult(
        vus=10_000,
        requests_per_second=5_000,
        http_error_rate_pct=0.5,
        p95_latency_ms=450,
        p99_latency_ms=700,
    )
    report = analyzer.evaluate(result)
    assert report["passed"]
    assert report["checks"]["p95_under_500ms"]
    assert report["checks"]["error_rate_under_1pct"]


def test_load_test_fails_when_p95_too_high():
    analyzer = LoadTestAnalyzer()
    result = LoadTestResult(
        vus=10_000,
        requests_per_second=5_000,
        http_error_rate_pct=0.5,
        p95_latency_ms=600,
        p99_latency_ms=900,
    )
    report = analyzer.evaluate(result)
    assert not report["passed"]
    assert not report["checks"]["p95_under_500ms"]
