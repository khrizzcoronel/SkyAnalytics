from src.security.dependency_scanner import DependencyScanner, Vulnerability


def test_no_findings_for_unknown_dependencies():
    scanner = DependencyScanner()
    findings = scanner.scan({"requests": "2.31.0"})
    assert findings == []


def test_detects_critical_vulnerability():
    vuln = Vulnerability(
        package="requests",
        installed_version="2.10.0",
        cve_id="CVE-2018-18074",
        cvss_score=9.8,
        fixed_version="2.20.0",
    )
    scanner = DependencyScanner(
        cve_database={"requests==2.10.0": [vuln]}
    )
    findings = scanner.scan({"requests": "2.10.0"})
    assert len(findings) == 1
    assert scanner.has_critical(findings)
    assert scanner.upgrade_plan(findings) == {"requests": "2.20.0"}
