"""
Create a deployment for the iris classification flow.
This is a boilerplate that needs to be completed as part of the challenge.
"""

import asyncio
import os
from prefect.runner.storage import GitRepository
from prefect_github import GitHubCredentials
from prefect import flow

WORK_POOL_NAME = "ml-pool"

def create_deployment():
    """Create deployment using GitHub source."""
    # TODO: Implement deployment creation
    # OPTION 1 : USING GITHUB REPOSITORY (remote flow)
    # 1. Load GitHub credentials from the block named "github-credentials"
    # 2. Get repository URL from GITHUB_REPOSITORY environment variable
    # 3. Create GitRepository object with:
    #    - URL from step 2
    #    - credentials from step 1
    #    - branch from GITHUB_BRANCH environment variable
    # 4. Create deployment from source:
    #    - source: github_repo
    #    - entrypoint: "flows/iris_flow_mlflow.py:iris_classification_flow"
    # 5. Deploy the flow with:
    #    - name: "iris-model"
    #    - work_pool_name: WORK_POOL_NAME
    #    - tags: ["ml", "iris"]
    #
    # OPTION 2 : USING LOCAL FLOW
    # 1. Create a local flow object from the iris_flow_mlflow.py file
    #    - source: local folder
    #    - entrypoint: "flows/iris_flow_mlflow.py:iris_classification_flow"
    # 2. Create deployment from source and deploy the flow with :
    #    - name: "iris-model-local"
    #    - work_pool_name: WORK_POOL_NAME
    #    - tags: ["ml", "iris", "local"]
    pass

if __name__ == "__main__":
    create_deployment()
    # Or asyncio.run(create_deployment()) if using await on objects
