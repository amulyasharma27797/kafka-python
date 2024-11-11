#!/bin/bash

# Wait until Kafka is reachable
while ! nc -z kafka 9092; do
  echo "Waiting for Kafka to be ready..."
  sleep 3
done

# Run the producer script after Kafka is ready
echo "Kafka is up - executing command"

exec $cmd
