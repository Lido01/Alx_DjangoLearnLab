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
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework import generics

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        followed_users = self.request.user.following.all()
        filtering = Post.objects.filter(user__in=followed_users).order_by('-created_at')
        return filtering

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from .models import Post, Like
from django.shortcuts import get_object_or_404
from notifications.models import Notification

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # Prevent duplicate likes
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'message': 'Already liked'}, status=400)
        Like.objects.create(user=request.user, post=post)
        # Create notification for the post owner
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb="liked your post",
            target=post
        )
        return Response({'message': 'Post liked'}, status=200)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({'message': 'Post unliked'}, status=200)
        return Response({'message': 'You have not liked this post'}, status=400)
