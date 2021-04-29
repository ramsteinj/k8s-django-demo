import logging
import datetime
import json

import django_filters
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser , IsAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import YogiyoUser
from .serializers import YogiyoUserSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)

# For swagger/redoc generation
user_sample = YogiyoUser(email="bob@yogiyo.com", username="bob", name="Bob James")
username_param = openapi.Parameter(
    'username',
    openapi.IN_PATH,
    description="Yogiyo User ID",
    type=openapi.TYPE_STRING,
    default='bob',
    required=True
)

search_param = openapi.Parameter(
    'keyword',
    openapi.IN_PATH,
    description="search keyword",
    type=openapi.TYPE_STRING,
    default='admin',
    required=True
)

# View Class
class YogiyoUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, username):
        logger.debug("username: %s", username)
        try:
            return YogiyoUser.objects.get(username=username)
        except YogiyoUser.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_id="Get user by username",
        manual_parameters=[username_param],
        responses={
            200: YogiyoUserSerializer,
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def get(self, request, username, format=None):
        logger.debug('YogiyoUserView.get() invoked...')
        user = self.get_object(username)
        serializer = YogiyoUserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id="Update user",
        manual_parameters=[username_param],
        request_body=YogiyoUserSerializer(user_sample),
        responses={
            201: YogiyoUserSerializer,
            400: "Bad Request"
        }
    )
    def put(self, request, username, format=None):
        logger.debug('YogiyoUserView.put() invoked...')
        user = self.get_object(username)
        serializer = YogiyoUserSerializer(user, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id="Delete user",
        manual_parameters=[username_param],
        responses={
            204: "No Content",
            401: "Unauthorized",
        }
    )
    def delete(self, request, username, format=None):
        logger.debug('YogiyoUserView.delete() invoked...')
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)