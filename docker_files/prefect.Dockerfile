# Prefect Dockerfile with pinned version for reproducibility
FROM prefecthq/prefect:3.1.11-python3.12

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install Python dependencies with correct pinned versions
RUN pip install --no-cache-dir \
    prefect-github==0.3.1 \
    scikit-learn==1.4.2 \
    pandas==2.2.2 \
    mlflow==3.1.1 \
    python-dotenv==1.0.1

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV PREFECT_HOME=/app/.prefect

# Default command
CMD ["prefect", "server", "start"]
