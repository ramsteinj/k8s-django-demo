#!/bin/sh

# switch to EKS - Fargate context
kubectl config use-context arn:aws:eks:ap-northeast-2:637107739800:cluster/yogiyo-forum

# undo the current rollout and rollback to the previous revision
kubectl rollout history deployment.v1.apps/backend --namespace=yogiyo
kubectl rollout history deployment.v1.apps/frontend --namespace=yogiyo