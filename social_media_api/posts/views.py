from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import Post , Comment

# Create your views here.
class PostViewSet(ViewSet):
    def get(self):
        pass
    def post(self):
        pass
