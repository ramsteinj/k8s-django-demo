#!/bin/sh

# switch to EKS - Fargate context
kubectl config use-context minikube

# deploy and run all applications on local minikube
skaffold dev -v info --port-forward # --no-prune=false --cache-artifacts=false