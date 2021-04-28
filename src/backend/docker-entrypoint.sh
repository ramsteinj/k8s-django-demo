#!/bin/bash

# Collect static files
#echo "Collecting static files..."
#python manage.py collectstatic

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Creat a super user
#python manage.py createsuperuser --email admin@yogiyo.com --username admin
#python manage.py syncdb --noinput
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@bsgglobal.com', 'password1234')" | python manage.py shell
echo "Adding default admin account if not exist..."
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()  # get the currently active user model,
User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@yogiyo.com', 'password1234')
User.objects.filter(username='bob').exists() or \
    User.objects.create_user('bob', 'bob@yogiyo.com', 'password1234', is_staff=True)
User.objects.filter(username='james').exists() or \
    User.objects.create_user('james', 'james@yogiyo.com', 'password1234', is_staff=True)
EOF

# echo "Adding 'AWS Region Location' default data to MongoDB Collection..."
# cat <<EOF | python manage.py shell
# from backend.utils.mongodb import MongoDB
# MongoDB().initialize_region_location()
# EOF

echo "Launching django server..."
python manage.py runserver 0.0.0.0:8000 --noreload