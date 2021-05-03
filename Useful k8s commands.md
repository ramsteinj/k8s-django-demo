# Useful minikube and kubectl commands

Here are the list of useful minikube and kubectl commands.

---

## How to start/stop/delete minikube cluster

~~~bash
# start minikube cluster
minikube start

# stop minikube cluster
minikube stop

# delete minikube cluster
minikube delete

# clean minikube cluster completely.
# --all: to delete all profiles
# --purge: delete the '~/.minikube' folder from your user directory.
minikube delete --all --purge
~~~

## How to access minikube node

~~~bash
# access to minikube node
minikube ssh
~~~

## How to check resource usages by minikube cluster

~~~bash
# CPU
minikube ssh -- top -b -n 1 | head -n 4

# Memory
minikube ssh -- free -m

# Disk
minikube ssh -- df -h /var/lib/docker
~~~

## How to prune disk that are used by minikube

~~~bash
docker system prune -a -f
~~~

## How to check minikube cluster status

~~~bash
# only for minikube
minikube ip
minikube status

# can be used in any k8s clusters
kubectl get componentstatuses
kubectl get nodes
kubectl describe nodes <node name>

# check resource usage stats
kubectl top nodes
kubectl top pods --namespace=cloudon
~~~

## How to launch minikube dashboard

~~~bash
# start minikube dashboard
minikube dashboard
~~~

## How to manage minikube addons

~~~bash
# show entire minikube addons
minikube addons list

# enable specific addon
minikube addons enable dashboard
minikube addons enable ingress
minikube addons enable ingress-dns
~~~

## How to check service endpoint url

~~~bash
minikube service list
minikube service <service name> --url
~~~

## How to check ingress address

~~~bash
kubectl get ingress cloudon-ingress --namespace cloudon
kubectl get ingress prometheus-ui --namespace monitoring
~~~

## How to get all kubernetes object list

~~~bash
kubectl api-resources
~~~

## How to check kubernetes auto-scaler status

~~~bash
kubectl get hpa
kubectl describe hpa rest-api --namespace=cloudon
kubectl describe hpa frontend --namespace=cloudon
~~~


## How to generate configmap yaml file from .env file

~~~bash
cd cloudon/kubernetes-manifests/local/1
kubectl create configmap cloudon-config --from-env-file=../../../src/.env --namespace=cloudon
kubectl get configmap cloudon-config -o yaml
~~~
