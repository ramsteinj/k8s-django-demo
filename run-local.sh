#!/bin/sh

# switch to EKS - Fargate context
kubectl config use-context minikube

# prepare to deploy application
skaffold dev -v info --port-forward # --no-prune=false --cache-artifacts=false

# deploy and run application
#skaffold run -v info --port-forward
