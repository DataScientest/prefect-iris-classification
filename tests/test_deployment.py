import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from prefect.testing.utilities import prefect_test_harness
from flows.iris_flow_mlflow import iris_classification_flow

def test_deployment_configuration():
    # Test if deployment is properly configured
    deployment = iris_classification_flow.to_deployment(
        name="test-deployment",
        work_pool_name="ml-pool"
    )
    
    assert deployment.name == "test-deployment"
    assert deployment.work_pool_name == "ml-pool"

def test_deployment_run():
    with prefect_test_harness():
        # Test if deployment can be run
        deployment = iris_classification_flow.to_deployment(
            name="test-deployment",
            work_pool_name="ml-pool"
        )
        assert deployment is not None