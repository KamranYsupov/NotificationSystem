from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactSerializer
from src.apps.notifications.tasks import send_message_task


class SendNotificationView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            send_message_task.delay(
                email=serializer.data['email'],
                phone_number=serializer.data['phone_number'],
                message=serializer.data['message'],
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
