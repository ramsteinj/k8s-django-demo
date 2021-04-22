#!/bin/sh

# execute docker-env
minikube docker-env

# set env variables
eval $(minikube -p minikube docker-env)

# run vscode
code workspace.code-workspace
