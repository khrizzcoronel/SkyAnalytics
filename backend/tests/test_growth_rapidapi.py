from src.growth.rapidapi_gateway import RapidApiGateway, RapidApiRequest, RapidPlan


def test_valid_secret_within_limit_allowed():
    gateway = RapidApiGateway(expected_secret="secret-123")
    request = RapidApiRequest(proxy_secret="secret-123", user="u1", plan=RapidPlan.FREEMIUM)
    assert gateway.allow_request(request)


def test_invalid_secret_rejected():
    gateway = RapidApiGateway(expected_secret="secret-123")
    request = RapidApiRequest(proxy_secret="wrong", user="u1", plan=RapidPlan.FREEMIUM)
    assert not gateway.allow_request(request)


def test_plan_hard_limit_enforced():
    gateway = RapidApiGateway(expected_secret="secret-123")
    user = "u2"
    request = RapidApiRequest(proxy_secret="secret-123", user=user, plan=RapidPlan.FREEMIUM)
    for _ in range(1_000):
        assert gateway.allow_request(request)
    assert not gateway.allow_request(request)
