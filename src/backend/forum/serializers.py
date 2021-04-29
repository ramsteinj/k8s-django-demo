import logging
from rest_framework import serializers
from .models import Forum, Discussion

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Serializers
class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['user', 'topic', 'description', 'created']

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ['forum', 'discuss', 'created']