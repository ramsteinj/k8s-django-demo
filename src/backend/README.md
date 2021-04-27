# Setting Development Environment
Below steps are needed to set up your local development environment.

## Install required softwares
Install required softwares as below:

~~~bash
# Install required softwares
brew install python3
brew install postgresql
brew install redis
~~~

> Note: Postgresql and redis are not used at all during development and deployment cycle. These are required for python psycopg2 and redis package installation only.

Optionally, you can install the below software for your convenience.

~~~bash
# Install optional softwares

# DBeaver: free multi-platform database tool for developers
brew install --cask dbeaver-community

~~~

## Set Python Virtual Environment
After the package installation, execute following commands to create a python virtual environment.

~~~bash
cd k8s-django-demo/src/backend

# Create a python virtual environment for project
python -m venv env
pip install pylint
source env/bin/activate
~~~

In VS Code, open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the ```> Python: Select Interpreter command:```

## Install Python Packages
Install python packages using pip as following:

~~~bash
# Install python packages
pip install django
pip install djangorestframework
pip install django-rest-auth
pip install django-allauth
pip install psycopg2
pip install django-filter
pip install redis
pip install django-redis-sessions
pip install markdown
pip install -U drf-yasg drf-yasg[validation]
pip install python-dateutil

# Save required packages into requirements.txt
pip freeze > requirements.txt
~~~

> Note: You can install all the required packages by executing "pip install -r requirements.txt" command as requirements.txt is already generated if you checked out this source code via "git clone".

## Create a Django Project

~~~bash
cd k8s-django-demo/src/backend

# Create the django project
django-admin startproject rest_api .

# Create the Restful API applications
cd rest_api
django-admin startapp users
~~~

> Note: You don't need to execute above commands if you checked out the project source code from git as those are already generated.