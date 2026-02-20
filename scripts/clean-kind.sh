#!/bin/bash
set -e
echo "Deleting Kind cluster..."
kind delete cluster --name aiops-cluster
echo "Cluster deleted."

