#!/bin/bash

# Collect static files
#echo "Collecting static files..."
#python manage.py collectstatic

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Creat a super user and a default forum
echo "Adding default admin account and a forum if not exist..."
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
from users.models import YogiyoUser
from forum.models import Forum
from forum.serializers import ForumSerializer

User = get_user_model()  # get the currently active user model,
User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@yogiyo.com', 'password1234')
User.objects.filter(username='bob').exists() or \
    User.objects.create_user('bob', 'bob@yogiyo.com', 'password1234', is_staff=True)
User.objects.filter(username='james').exists() or \
    User.objects.create_user('james', 'james@yogiyo.com', 'password1234', is_staff=True)

Forum.objects.filter(forum_id=1).exists() or \
    Forum.objects.create(user_id=YogiyoUser.objects.get(username='admin'), topic='Yogiyo Smalltalk', description='auto generated default forum')
EOF

# echo "Adding 'AWS Region Location' default data to MongoDB Collection..."
# cat <<EOF | python manage.py shell
# from backend.utils.mongodb import MongoDB
# MongoDB().initialize_region_location()
# EOF