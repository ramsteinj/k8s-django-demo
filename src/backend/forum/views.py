import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import Forum, Discussion
from .serializers import ForumSerializer, DiscussionSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


class ForumListView(APIView):
    """
    List all forums
    """
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_id="List all forums",
        #operation_description="List all existing forums created. \
        #                         \n- Requires token authentication. \
        #                         \n- Requires admin previeledge.",
        operation_description="List all existing forums created. \
                                 \n- Requires token authentication.",
        # query_serializer=LoginHistorySerializer,
        responses={
            200: ForumSerializer(many=True),
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def get(self, request, format=None):
        logger.debug('ForumListView.get() invoked...')
        forums = Forum.objects.all()
        serializers = ForumSerializer(forums, many=True)
        return Response(serializers.data)
