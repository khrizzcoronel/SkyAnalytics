from src.security.secret_scanner import SecretScanner


def test_clean_content_passes():
    scanner = SecretScanner()
    result = scanner.scan("const apiUrl = 'https://example.com';", "config.ts")
    assert result.clean


def test_detects_aws_access_key():
    scanner = SecretScanner()
    result = scanner.scan("aws_access_key_id = 'AKIAIOSFODNN7EXAMPLE';", "config.py")
    assert not result.clean
    assert any("aws_access_key" in finding for finding in result.findings)


def test_detects_private_key():
    scanner = SecretScanner()
    result = scanner.scan("-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA...", "key.pem")
    assert not result.clean
    assert any("private_key" in finding for finding in result.findings)
