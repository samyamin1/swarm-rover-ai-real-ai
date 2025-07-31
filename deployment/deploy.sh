#!/bin/bash

# Simple deployment script for Swarm Rover AI

echo "Building Docker images..."
docker-compose build

echo "Starting Docker containers..."
docker-compose up -d

echo "Swarm Rover AI deployed successfully!"
echo "You can access the simulation via the exposed port (if any) or by interacting with the running containers."

# Optional: Add commands for Kubernetes deployment if kubernetes.yaml is configured
# echo "Deploying to Kubernetes..."
# kubectl apply -f kubernetes.yaml
