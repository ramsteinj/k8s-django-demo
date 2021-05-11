#!/bin/sh

# switch to EKS - Fargate context
kubectl config use-context arn:aws:eks:ap-northeast-2:946019410907:cluster/yogiyo-forum

# delete cloudon applications from EKS - Fargate
skaffold delete --namespace=yogiyo