#!/bin/bash
set -e

IMAGE_NAME=aiops-app:latest

echo "Building Docker image..."
docker build -t $IMAGE_NAME ./docker

echo "Loading image into Kind..."
kind load docker-image $IMAGE_NAME --name aiops-cluster

echo "Deploying Helm chart..."
helm upgrade --install aiops-app helm/aiops-app

echo "Deployment complete."
kubectl get pods
kubectl get svc

