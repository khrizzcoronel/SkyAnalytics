"""
OpenAPI contract validator for CI/CD.

Performs lightweight static checks that mirror what Spectral/openapi-diff
do: style guide enforcement and breaking-change detection between two specs.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class ValidationReport:
    valid: bool = True
    style_errors: List[str] = field(default_factory=list)
    breaking_changes: List[str] = field(default_factory=list)

    def add_style_error(self, message: str) -> None:
        self.style_errors.append(message)
        self.valid = False

    def add_breaking_change(self, message: str) -> None:
        self.breaking_changes.append(message)
        self.valid = False


class OpenAPIValidator:
    """Validate an OpenAPI spec against style rules and detect breaking changes."""

    SNAKE_CASE_RE = "^[a-z_][a-z0-9_]*$"

    def __init__(self, base_spec: Dict[str, Any]):
        self.base_spec = base_spec

    def validate(self, new_spec: Dict[str, Any]) -> ValidationReport:
        report = ValidationReport()
        self._check_style(new_spec, report)
        self._detect_breaking_changes(new_spec, report)
        return report

    def _check_style(self, spec: Dict[str, Any], report: ValidationReport) -> None:
        paths = spec.get("paths", {})
        if not paths:
            report.add_style_error("No paths defined in spec")
            return

        for path, methods in paths.items():
            for method, operation in methods.items():
                if method in ("parameters", "summary", "description"):
                    continue
                if not isinstance(operation, dict):
                    continue
                if not operation.get("summary"):
                    report.add_style_error(
                        f"{method.upper()} {path}: missing summary"
                    )
                if not operation.get("description"):
                    report.add_style_error(
                        f"{method.upper()} {path}: missing description"
                    )
                responses = operation.get("responses", {})
                for code in ("200", "400"):
                    if code not in responses:
                        report.add_style_error(
                            f"{method.upper()} {path}: missing example response {code}"
                        )

    def _detect_breaking_changes(
        self, new_spec: Dict[str, Any], report: ValidationReport
    ) -> None:
        base_paths = self.base_spec.get("paths", {})
        new_paths = new_spec.get("paths", {})

        # Removed endpoints
        for path in base_paths:
            if path not in new_paths:
                report.add_breaking_change(f"Removed endpoint: {path}")
                continue
            base_methods = {
                m for m in base_paths[path] if m not in ("parameters", "summary", "description")
            }
            new_methods = {
                m for m in new_paths[path] if m not in ("parameters", "summary", "description")
            }
            for method in base_methods - new_methods:
                report.add_breaking_change(f"Removed method: {method.upper()} {path}")

        # Removed required response fields (only one level deep for simplicity)
        for path, methods in base_paths.items():
            if path not in new_paths:
                continue
            for method, base_op in methods.items():
                if method in ("parameters", "summary", "description"):
                    continue
                new_op = new_paths[path].get(method)
                if not isinstance(new_op, dict):
                    continue
                base_schema = self._response_schema(base_op)
                new_schema = self._response_schema(new_op)
                if base_schema and new_schema:
                    base_props = set(base_schema.get("properties", {}).keys())
                    new_props = set(new_schema.get("properties", {}).keys())
                    for removed_prop in base_props - new_props:
                        report.add_breaking_change(
                            f"Removed response property '{removed_prop}' in {method.upper()} {path}"
                        )

    @staticmethod
    def _response_schema(operation: Dict[str, Any]) -> Dict[str, Any]:
        response = operation.get("responses", {}).get("200", {})
        content = response.get("content", {})
        for media_type in ("application/json", "application/json; charset=utf-8"):
            if media_type in content:
                return content[media_type].get("schema", {})
        return {}
