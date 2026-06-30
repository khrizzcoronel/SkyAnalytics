from src.tactical.mlops_registry import ModelRegistry


def test_register_requires_shap():
    registry = ModelRegistry()
    assert registry.register_run("model_v1", mape=12.0, has_shap=False) is False
    assert "model_v1" not in registry.models


def test_promote_blocks_high_mape():
    registry = ModelRegistry()
    registry.register_run("model_v2", mape=18.2, has_shap=True)
    assert registry.promote_model("model_v2", "Production") is False
    assert registry.models["model_v2"]["stage"] == "Staging"


def test_promote_allows_good_mape():
    registry = ModelRegistry()
    registry.register_run("model_v3", mape=10.5, has_shap=True)
    assert registry.promote_model("model_v3", "Production") is True
    assert registry.models["model_v3"]["stage"] == "Production"
