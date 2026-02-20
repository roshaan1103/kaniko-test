#!/bin/bash
set -e

echo "Creating Kind cluster..."
kind create cluster --config k8s/kind-config.yaml --name aiops-cluster
kubectl cluster-info --context kind-aiops-cluster
echo "Kind cluster is ready."

