# Dockerfile
FROM python:3.9-slim

# Install netcat (nc) for the wait-for-kafka script
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy pyka-scripts dir to container
COPY /pyka-scripts/ .

# Set execute permissions for wait-for-kafka.sh
RUN chmod +x wait_for_kafka.sh

# Set PYTHONPATH to /app/pyka-scripts
ENV PYTHONPATH=/app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt
