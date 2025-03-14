from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer 
from .models import Author, Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class ProtecteView(LoginRequiredMixin, View):
    login_url = "/login/"# By default is says this but you can cutomize other html file and add in url.py
    redirect_field_name = "next"

    def get(self, request, **args):
        return render(request, "templates/home.html", {'context': "This page is only used for logged in user"})
class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()