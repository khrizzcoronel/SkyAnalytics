"""
Terraform policy validator.

Checks that Terraform modules enforce mandatory tags and prevent destruction
of production stateful resources.
"""
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class TerraformResource:
    resource_type: str
    name: str
    config: Dict
    environment: str = "unknown"


@dataclass
class PolicyReport:
    valid: bool = True
    violations: List[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.violations.append(message)
        self.valid = False


class TerraformPolicyValidator:
    """Validate Terraform resources against FinOps and security policies."""

    REQUIRED_TAGS = {"Environment", "Project", "Owner", "ManagedBy"}

    def validate(self, resources: List[TerraformResource]) -> PolicyReport:
        report = PolicyReport()
        for resource in resources:
            tags = resource.config.get("tags", {})
            missing = self.REQUIRED_TAGS - set(tags.keys())
            if missing:
                report.add(
                    f"{resource.resource_type}.{resource.name}: missing tags {missing}"
                )

            if resource.environment.lower() == "production":
                lifecycle = resource.config.get("lifecycle", {})
                if not lifecycle.get("prevent_destroy"):
                    report.add(
                        f"{resource.resource_type}.{resource.name}: production resource missing prevent_destroy"
                    )

            if resource.resource_type == "aws_s3_bucket":
                acl = resource.config.get("acl")
                if acl == "public-read":
                    report.add(
                        f"{resource.resource_type}.{resource.name}: public S3 bucket prohibited"
                    )

        return report
