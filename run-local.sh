#!/bin/sh

# Image tag for docker container in development environment
export IMAGE_TAG_FOR_DEV="dev"

# switch to EKS - Fargate context
kubectl config use-context minikube

# deploy and run all applications on local minikube
skaffold dev -v info --port-forward # --no-prune=false --cache-artifacts=false