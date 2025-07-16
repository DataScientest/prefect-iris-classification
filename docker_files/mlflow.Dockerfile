# MLflow Dockerfile with pinned version for reproducibility
FROM python:3.12.7-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install MLflow with pinned version
RUN pip install --no-cache-dir \
    mlflow==3.1.1 \
    psycopg2-binary==2.9.9 \
    boto3==1.34.34

# Create MLflow user
RUN useradd -m -u 1000 mlflow-user

# Create MLflow directories
RUN mkdir -p /mlruns /mlflow && \
    chown -R mlflow-user:mlflow-user /mlruns /mlflow

# Switch to MLflow user
USER mlflow-user

# Set working directory
WORKDIR /mlflow

# Expose port
EXPOSE 5000

# Default command
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000", "--default-artifact-root", "/mlruns", "--serve-artifacts"]
