#!/bin/bash

# Start the django server.
if [ $DJANGO_DEBUG == "True" ] then
    # Note that --noreload option disables the auto-reloader (any python code change is not applied while the server is running)
    # as Skaffold will do this.
    echo "Running django server in development mode..."
    python manage.py runserver “0.0.0.0:8000” —noreload
else
    #python manage.py check --deploy
    # Configure nginx - uwsgi - django
    echo "Running django server in production mode..."
fi