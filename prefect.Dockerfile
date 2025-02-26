FROM prefecthq/prefect:3-latest

# Install curl for healthcheck and required Python packages
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* && \
    pip install prefect-github scikit-learn pandas mlflow