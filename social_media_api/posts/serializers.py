from rest_framework import serializers
from .models import Post, Comment

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title",]