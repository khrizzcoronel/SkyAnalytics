"""
Secret scanner for CI/CD pre-commit / pipeline checks.

Detects high-entropy tokens and common secret patterns to prevent
accidental credential leaks.
"""
import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class SecretScanResult:
    clean: bool = True
    findings: List[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.findings.append(message)
        self.clean = False


class SecretScanner:
    """Scan text for patterns that resemble leaked secrets."""

    PATTERNS = {
        "aws_access_key": re.compile(r"AKIA[0-9A-Z]{16}"),
        "aws_secret_key": re.compile(r"['\"\s]([A-Za-z0-9/+=]{40})['\"\s]"),
        "generic_api_key": re.compile(
            r"(?:api[_-]?key|apikey|token)\s*[:=]\s*['\"]([a-zA-Z0-9_\-]{32,})['\"]",
            re.IGNORECASE,
        ),
        "private_key": re.compile(r"-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"),
    }

    def scan(self, content: str, filename: str = "<unknown>") -> SecretScanResult:
        result = SecretScanResult()
        for name, pattern in self.PATTERNS.items():
            for match in pattern.finditer(content):
                snippet = content[max(0, match.start() - 10):match.end() + 10]
                result.add(
                    f"{filename}: possible {name} leak near '{snippet}'"
                )
        return result
