from src.devex.openapi_validator import OpenAPIValidator


BASE_SPEC = {
    "openapi": "3.1.0",
    "info": {"title": "SkyAnalytics API", "version": "v1.0.0"},
    "paths": {
        "/api/v1/flights": {
            "get": {
                "summary": "List flights",
                "description": "Returns a list of flights",
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "flight_id": {"type": "string"},
                                        "delay_minutes": {"type": "integer"},
                                    },
                                }
                            }
                        },
                    },
                    "400": {"description": "Bad Request"},
                },
            }
        }
    },
}


def test_valid_spec_passes():
    validator = OpenAPIValidator(BASE_SPEC)
    report = validator.validate(BASE_SPEC)
    assert report.valid
    assert not report.style_errors
    assert not report.breaking_changes


def test_missing_summary_is_style_error():
    new_spec = {
        **BASE_SPEC,
        "paths": {
            "/api/v1/flights": {
                "get": {
                    "description": "Returns a list of flights",
                    "responses": {
                        "200": {"description": "OK"},
                        "400": {"description": "Bad Request"},
                    },
                }
            }
        },
    }
    validator = OpenAPIValidator(BASE_SPEC)
    report = validator.validate(new_spec)
    assert not report.valid
    assert any("missing summary" in err for err in report.style_errors)


def test_removed_endpoint_is_breaking_change():
    new_spec = {
        **BASE_SPEC,
        "paths": {},
    }
    validator = OpenAPIValidator(BASE_SPEC)
    report = validator.validate(new_spec)
    assert not report.valid
    assert any("Removed endpoint" in err for err in report.breaking_changes)


def test_removed_response_property_is_breaking_change():
    new_spec = {
        **BASE_SPEC,
        "paths": {
            "/api/v1/flights": {
                "get": {
                    "summary": "List flights",
                    "description": "Returns a list of flights",
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "flight_id": {"type": "string"},
                                        },
                                    }
                                }
                            },
                        },
                        "400": {"description": "Bad Request"},
                    },
                }
            }
        },
    }
    validator = OpenAPIValidator(BASE_SPEC)
    report = validator.validate(new_spec)
    assert not report.valid
    assert any("delay_minutes" in err for err in report.breaking_changes)
