#!/bin/sh

# switch to EKS - Fargate context
kubectl config use-context arn:aws:eks:ap-northeast-2:946019410907:cluster/yogiyo-forum

# prepare to deploy application to EKS
skaffold run -v info --default-repo 946019410907.dkr.ecr.ap-northeast-2.amazonaws.com/yogiyo