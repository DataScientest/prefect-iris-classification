import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prefect_github import GitHubCredentials
from prefect_github.repository import GitHubRepository
from flows.iris_flows import iris_classification_flow

# Load GitHub blocks
github_credentials = GitHubCredentials.load("github-credentials")

# Adapt the name of the creadentials block you created
github_repository = GitHubRepository.load("github-blocks")

# Ensure repository has credentials
github_repository.credentials = github_credentials

if __name__ == "__main__":
    # Deploy the flow
    iris_classification_flow.from_source(
        source=github_repository,
        entrypoint="flows/iris_flows.py:iris_classification_flow"
    ).deploy(
        name="iris-model-prod",
        tags=["ml", "production"],
        version="1", # Increment version number for each deployment
        work_pool_name="local-pool"
    )