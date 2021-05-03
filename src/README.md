# Launching Application in Development Mode

Developing a django application on minikube is not ideal because:
 - **Too Heavy**: Minikube is a lightweight Kubernetes implementation that creates a VM on local machine but still heavy as it is a kubernetes cluster.
 - **Django Migration Issue**: Whenever django ORM model changes, DB migration scripts should be generated in the migrations folder that migrate the database from its current state to the new state. However, these migration scripts can not be generated as the django application runs in a kubernetes pod.

For those reasons, we use docker-compose for deveopment purpose and use minikube for deployment test in local environment.

## Prerequisites
- **Docker for Mac**: [Installation](https://docs.docker.com/docker-for-mac/install/)

## How to launch

Before you execute docker-compose, make sure that "Docker for Mac" is up and running.

~~~bash
cd k8s-django-demo/src
./start-local.sh
~~~

## How to stop

~~~bash
cd k8s-django-demo/src
./stop-local.sh
~~~

## Django Migration

Whenever django model changes, apply changes to the database as below:

~~~bash
cd k8s-django-demo/src
./db_migrate.sh
~~~


## How to access
 - [Frontend](http://localhost:8080)
 - [Backend Swagger](http://localhost:8000/swagger)
 - [Backend Redoc](http://localhost:8000/redoc)