"""
Dependency vulnerability scanner.

Abstract interface for SCA tools (Snyk/Dependabot). The in-memory adapter
allows tests to simulate CVE findings.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Vulnerability:
    package: str
    installed_version: str
    cve_id: str
    cvss_score: float
    fixed_version: Optional[str] = None


class DependencyScanner:
    """Detect vulnerable dependencies against a known CVE database."""

    CRITICAL_CVSS_THRESHOLD = 7.0

    def __init__(self, cve_database: Optional[Dict[str, List[Vulnerability]]] = None):
        self._db = cve_database or {}

    def scan(
        self,
        dependencies: Dict[str, str],
    ) -> List[Vulnerability]:
        findings: List[Vulnerability] = []
        for package, version in dependencies.items():
            key = f"{package}=={version}"
            findings.extend(self._db.get(key, []))
        return findings

    def has_critical(self, findings: List[Vulnerability]) -> bool:
        return any(v.cvss_score > self.CRITICAL_CVSS_THRESHOLD for v in findings)

    def upgrade_plan(
        self,
        findings: List[Vulnerability],
    ) -> Dict[str, str]:
        """Return package -> fixed_version mapping."""
        plan: Dict[str, str] = {}
        for vuln in findings:
            if vuln.fixed_version:
                plan[vuln.package] = vuln.fixed_version
        return plan
