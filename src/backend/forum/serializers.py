import logging
from rest_framework import serializers
from .models import Forum, Discussion
from users.models import YogiyoUser
from users.serializers import YogiyoUserSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Serializers
class ForumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forum
        fields = ['user_id', 'forum_id', 'topic', 'description', 'created']

class ForumListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    def get_username(self, forum):
        return str(forum.user_id)

    class Meta:
        model = Forum
        fields = ['user_id', 'username', 'forum_id', 'topic', 'description', 'created']


class DiscussionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discussion
        fields = ['user_id', 'forum_id', 'discussion_id', 'discuss', 'created']


class DiscussionListSerializer(serializers.ModelSerializer):
    #user = YogiyoUserSerializer(many=False, read_only=True)
    # username = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='YogiyoUser.username'
    # )
    #forum = ForumSerializer(many=False, read_only=True)
    username = serializers.SerializerMethodField('get_username')

    def get_username(self, discussion):
        return str(discussion.user_id)

    class Meta:
        model = Discussion
        fields = ['user_id', 'username', 'forum_id', 'discussion_id', 'discuss', 'created']
