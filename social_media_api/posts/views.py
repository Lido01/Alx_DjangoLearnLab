from django.shortcuts import render
from rest_framework import viewsets
from .models import Post , Comment
from .serializers import PostSerializers, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    # def get(self):
    #     pass
    # def post(self):
    #     pass

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#Feed Function View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework import generics

class FeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        followed_users = self.request.user.following.all()
        return Post.objects.filter(user__in=followed_users).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
