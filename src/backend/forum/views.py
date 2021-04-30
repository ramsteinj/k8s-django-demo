import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import Forum, Discussion
from .serializers import ForumSerializer, DiscussionSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Forum & Discussion View
class ForumListView(APIView):
    """
    List all forums
    """
    #renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        operation_id="List all forums",
        operation_description="List all existing forums created. \
                                 \n- Requires token authentication.",
        responses={
            200: ForumSerializer(many=True),
            401: "Unauthorized"
        }
    )
    def get(self, request, format=None):
        logger.debug('ForumListView.get() invoked...')
        forums = Forum.objects.all()
        serializers = ForumSerializer(forums, many=True)
        return Response(serializers.data)

class ForumView(APIView):
    """
    Create/Delete/Update a forum
    """
    #renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_id="Create a forum",
        operation_description="Create a forum. \
                                 \n- Requires token authentication. \
                                 \n- Requires admin previeledge.",
        request_body=ForumSerializer,
        #query_serializer=ForumSerializer,
        responses={
            200: ForumSerializer(many=True),
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def post(self, request, format=None):
        logger.debug('ForumListView.post() invoked...')
        serializer = ForumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiscussionListView(APIView):
    """
    List all discussions
    """
    #renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        operation_id="List all discussions",
        operation_description="List all discussions in a forum. \
                                 \n- Requires token authentication.",
        responses={
            200: DiscussionSerializer(many=True),
            401: "Unauthorized"
        }
    )
    def get(self, request, forum_id, format=None):
        logger.debug('DiscussionListView.get(%d) invoked...', forum_id)
        try:
            discussion = Discussion.objects.filter(forum_id=forum_id)
        except Discussion.DoesNotExist:
            discussion = None
        serializers = DiscussionSerializer(discussion, many=True)
        return Response(serializers.data)

class DiscussionView(APIView):
    """
    Create/Delete/Update a discussion
    """
    #renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_id="Create a discussion",
        operation_description="Create a discussion. \
                                 \n- Requires token authentication. \
                                 \n- Requires admin previeledge.",
        request_body=DiscussionSerializer,
        responses={
            200: DiscussionSerializer(many=True),
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def post(self, request, format=None):
        logger.debug('DiscussionView.post() invoked...')
        serializer = DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)