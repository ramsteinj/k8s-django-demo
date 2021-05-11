#!/bin/bash

./backend-init.sh

# The suggested number of workers is (2*CPU)+1
echo "Launching django-gunicorn server..."
gunicorn rest_api.wsgi:application \
            --workers=5 \
            --bind 0.0.0.0:8001