"""
Changelog generator for the weekly Developer Portal release notes.

Parses conventional commits and produces a structured changelog entry
with semantic version bump rules.
"""
import re
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class ChangeType(Enum):
    BREAKING = "breaking"
    FEATURE = "feat"
    FIX = "fix"
    DOCS = "docs"
    CHORE = "chore"
    CI = "ci"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Commit:
    sha: str
    message: str
    pr_number: Optional[int] = None


@dataclass
class ChangelogEntry:
    version: str
    features: List[str] = field(default_factory=list)
    fixes: List[str] = field(default_factory=list)
    breaking: List[str] = field(default_factory=list)
    docs: List[str] = field(default_factory=list)

    def has_public_changes(self) -> bool:
        return any(
            [self.features, self.fixes, self.breaking, self.docs]
        )

    def to_markdown(self, repo_url: str = "https://github.com/org/repo") -> str:
        lines = [f"## {self.version}", ""]

        def linkify(text: str) -> str:
            match = re.search(r"\(#(\d+)\)", text)
            if match:
                pr = match.group(1)
                url = f"{repo_url}/pull/{pr}"
                return re.sub(r"\(#\d+\)", f"([#{pr}]({url}))", text)
            return text

        if self.breaking:
            lines.extend(["### ⚠ Breaking Changes", ""])
            lines.extend(f"- {linkify(item)}" for item in self.breaking)
            lines.append("")
        if self.features:
            lines.extend(["### ✨ Features", ""])
            lines.extend(f"- {linkify(item)}" for item in self.features)
            lines.append("")
        if self.fixes:
            lines.extend(["### 🐛 Bug Fixes", ""])
            lines.extend(f"- {linkify(item)}" for item in self.fixes)
            lines.append("")
        if self.docs:
            lines.extend(["### 📝 Documentation", ""])
            lines.extend(f"- {linkify(item)}" for item in self.docs)
            lines.append("")
        return "\n".join(lines).strip()


class ChangelogGenerator:
    """Generate changelog entries from conventional commits."""

    CONVENTIONAL_RE = re.compile(
        r"^(?P<type>feat|fix|docs|chore|ci|breaking)(?:\([^)]+\))?:\s*(?P<desc>.+)$",
        re.IGNORECASE,
    )
    PR_RE = re.compile(r"\(#(?P<pr>\d+)\)")
    BREAKING_RE = re.compile(r"BREAKING CHANGE[:]", re.IGNORECASE)

    def __init__(self, repo_url: str = "https://github.com/org/repo"):
        self.repo_url = repo_url

    def _classify(self, message: str) -> ChangeType:
        if self.BREAKING_RE.search(message):
            return ChangeType.BREAKING
        match = self.CONVENTIONAL_RE.match(message)
        if not match:
            return ChangeType.UNKNOWN
        try:
            return ChangeType(match.group("type").lower())
        except ValueError:
            return ChangeType.UNKNOWN

    def generate(
        self,
        current_version: str,
        commits: List[Commit],
    ) -> Optional[ChangelogEntry]:
        """Generate a changelog entry and bump the semantic version."""
        entry = ChangelogEntry(version=current_version)
        has_breaking = False

        for commit in commits:
            change_type = self._classify(commit.message)
            if change_type in (ChangeType.CHORE, ChangeType.CI, ChangeType.UNKNOWN):
                continue

            line = commit.message.strip()
            if change_type == ChangeType.BREAKING:
                has_breaking = True
                entry.breaking.append(self._strip_prefix(line))
            elif change_type == ChangeType.FEATURE:
                entry.features.append(self._strip_prefix(line))
            elif change_type == ChangeType.FIX:
                entry.fixes.append(self._strip_prefix(line))
            elif change_type == ChangeType.DOCS:
                entry.docs.append(self._strip_prefix(line))

        if not entry.has_public_changes():
            return None

        entry.version = self._bump_version(current_version, has_breaking)
        return entry

    @staticmethod
    def _bump_version(version: str, major: bool) -> str:
        parts = [int(p) for p in version.lstrip("v").split(".")]
        if len(parts) != 3:
            parts = [0, 0, 0]
        major_v, minor, patch = parts
        if major:
            return f"v{major_v + 1}.0.0"
        return f"v{major_v}.{minor + 1}.0"

    @staticmethod
    def _strip_prefix(message: str) -> str:
        match = re.match(r"^(?:feat|fix|docs|chore|ci|breaking)(?:\([^)]+\))?!?:\s*", message, re.IGNORECASE)
        if match:
            return message[match.end():].strip()
        return message.strip()
