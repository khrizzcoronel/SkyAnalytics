from datetime import datetime

from src.security.alert_router import AlertRouter, SecurityEvent, Severity, Action


def test_brute_force_event_is_blocked():
    router = AlertRouter()
    event = SecurityEvent(
        event_type="brute_force",
        source_ip="192.0.2.100",
        details="500 failed logins in 1 minute",
    )
    alert = router.handle(event)
    assert alert.severity == Severity.SEV3
    assert Action.BLOCK_IP in alert.actions
    assert "192.0.2.100" in router.blocked_ips


def test_crypto_mining_triggers_page():
    router = AlertRouter()
    event = SecurityEvent(
        event_type="crypto_mining",
        source_ip="10.0.0.5",
        details="crypto miner detected in pod",
    )
    alert = router.handle(event)
    assert alert.severity == Severity.SEV1
    assert Action.PAGE in alert.actions


def test_whitelisted_ip_is_not_blocked():
    router = AlertRouter(whitelisted_ips={"192.0.2.1"})
    event = SecurityEvent(
        event_type="brute_force",
        source_ip="192.0.2.1",
        details="failed logins",
    )
    alert = router.handle(event)
    assert Action.BLOCK_IP not in alert.actions
    assert "192.0.2.1" not in router.blocked_ips
