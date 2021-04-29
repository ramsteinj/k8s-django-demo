import logging
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import YogiyoUser

# get logger
logger = logging.getLogger(__name__)

class YogiyoUserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = YogiyoUser
        fields = ['id', 'password', 'email', 'username', 'groups', 'name']

    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data.get('password'))
    #     return super(UserSerializer, self).create(validated_data)

    # def update(self, instance, validated_data):
    #     change_password = validated_data.get('password')
    #     if change_password:
    #         validated_data['password'] = make_password(change_password)
    #     else:
    #         validated_data['password'] = instance.password
    #     return super(UserSerializer, self).update(instance, validated_data)