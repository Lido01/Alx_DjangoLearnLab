from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        unread_count = notifications.filter(read=False).count()
        response_data = {
            'unread_count': unread_count,
            'notifications': [
                {
                    'id': n.id,
                    'actor': n.actor.username,
                    'verb': n.verb,
                    'timestamp': n.timestamp,
                    'read': n.read
                } for n in notifications
            ]
        }
        return Response(response_data, status=200)