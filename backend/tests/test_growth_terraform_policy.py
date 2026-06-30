from src.growth.terraform_policy import TerraformPolicyValidator, TerraformResource


def test_valid_resource_passes():
    validator = TerraformPolicyValidator()
    resources = [
        TerraformResource(
            resource_type="aws_instance",
            name="web",
            environment="production",
            config={
                "tags": {
                    "Environment": "production",
                    "Project": "sky",
                    "Owner": "sre",
                    "ManagedBy": "Terraform",
                },
                "lifecycle": {"prevent_destroy": True},
            },
        )
    ]
    report = validator.validate(resources)
    assert report.valid


def test_missing_tags_and_public_bucket_flagged():
    validator = TerraformPolicyValidator()
    resources = [
        TerraformResource(
            resource_type="aws_s3_bucket",
            name="docs",
            environment="staging",
            config={
                "tags": {"Environment": "staging"},
                "acl": "public-read",
            },
        )
    ]
    report = validator.validate(resources)
    assert not report.valid
    assert any("missing tags" in v for v in report.violations)
    assert any("public S3 bucket" in v for v in report.violations)


def test_production_without_prevent_destroy_flagged():
    validator = TerraformPolicyValidator()
    resources = [
        TerraformResource(
            resource_type="aws_db_instance",
            name="main",
            environment="production",
            config={
                "tags": {
                    "Environment": "production",
                    "Project": "sky",
                    "Owner": "sre",
                    "ManagedBy": "Terraform",
                }
            },
        )
    ]
    report = validator.validate(resources)
    assert not report.valid
    assert any("prevent_destroy" in v for v in report.violations)
