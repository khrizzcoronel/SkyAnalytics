"""
SDK release version calculator.

Determines the next semantic version for SDKs and docs based on whether
a release contains breaking changes.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class SDKRelease:
    language: str
    current_version: str
    next_version: str
    package_name: str


class SDKReleasePlanner:
    """Plan SDK releases for Python, JavaScript and Java."""

    LANGUAGES = {
        "python": "skyanalytics-python",
        "javascript": "skyanalytics-node",
        "java": "skyanalytics-java",
    }

    def plan(
        self,
        current_version: str,
        breaking_change: bool,
    ) -> list[SDKRelease]:
        next_version = self._bump(current_version, breaking_change)
        return [
            SDKRelease(
                language=lang,
                current_version=current_version,
                next_version=next_version,
                package_name=name,
            )
            for lang, name in self.LANGUAGES.items()
        ]

    @staticmethod
    def _bump(version: str, major: bool) -> str:
        parts = [int(p) for p in version.lstrip("v").split(".")]
        if len(parts) != 3:
            parts = [0, 0, 0]
        major_v, minor, patch = parts
        if major:
            return f"v{major_v + 1}.0.0"
        return f"v{major_v}.{minor + 1}.0"
