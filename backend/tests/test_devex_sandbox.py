from src.devex.sandbox_token_bucket import SandboxRateLimiter


def test_allows_requests_up_to_limit():
    limiter = SandboxRateLimiter(max_requests_per_minute=3)
    token = "sandbox-token-123"
    assert limiter.allow_request(token)
    assert limiter.allow_request(token)
    assert limiter.allow_request(token)
    assert not limiter.allow_request(token)


def test_reset_restores_bucket():
    limiter = SandboxRateLimiter(max_requests_per_minute=1)
    token = "sandbox-token-456"
    assert limiter.allow_request(token)
    assert not limiter.allow_request(token)
    limiter.reset(token)
    assert limiter.allow_request(token)
