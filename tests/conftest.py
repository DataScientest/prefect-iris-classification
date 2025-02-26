import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ["PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS"] = "60"

import pytest
import os
import mlflow
from prefect.testing.utilities import prefect_test_harness

@pytest.fixture(autouse=True)
def setup_mlflow():
    # Set up MLflow for testing
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    yield
    # Clean up after tests
    if os.path.exists("mlflow.db"):
        os.remove("mlflow.db")

@pytest.fixture(autouse=True)
def setup_prefect():
    # Set up Prefect for testing
    with prefect_test_harness():
        yield