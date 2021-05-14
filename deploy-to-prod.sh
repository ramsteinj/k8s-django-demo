#!/bin/sh

# switch to EKS - Fargate context
kubectl config use-context arn:aws:eks:ap-northeast-2:637107739800:cluster/yogiyo-forum

# prepare to deploy application to EKS
skaffold run -v info -p=prod --default-repo 637107739800.dkr.ecr.ap-northeast-2.amazonaws.com/yogiyo-forum