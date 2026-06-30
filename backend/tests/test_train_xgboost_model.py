import os
import tempfile

import boto3
import pandas as pd
import numpy as np

from src.ml import train_xgboost_model as train_module


def test_train_xgboost_with_mock_data(monkeypatch, tmp_path):
    monkeypatch.setenv("ML_FALLBACK_MOCK", "true")
    monkeypatch.setattr(train_module, "S3_ML_BUCKET", "test-bucket")

    class FakeS3:
        def download_file(self, *args, **kwargs):
            raise Exception("no s3")
        def upload_file(self, *args, **kwargs):
            pass

    monkeypatch.setattr(boto3, "client", lambda service: FakeS3())

    # Cambiar al directorio temporal para no dejar residuos
    monkeypatch.chdir(tmp_path)

    train_module.train_xgboost()

    assert (tmp_path / "xgboost_delay_model.pkl").exists()
