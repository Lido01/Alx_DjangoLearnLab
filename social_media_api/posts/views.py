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