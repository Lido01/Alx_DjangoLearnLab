from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer 
from .models import Author, Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework


class ProtecteView(LoginRequiredMixin, View):
    login_url = "/login/"# By default is says this but you can cutomize other html file and add in url.py
    redirect_field_name = "next"

    def get(self, request, **args):
        return render(request, "templates/home.html", {'context': "This page is only used for logged in user"})
class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]
    filter_backends =  [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields =  ["title"]
    search_fields = ["title", "author"]
    ordering_fields = ["title", "publication_year"]


class DetailView(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
class CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]
    authentication_classes = SessionAuthentication, BasicAuthentication
    serializer_class = BookSerializer
    
    # Customize the view by form submissions and data validation
    queryset = Book.objects.all()
class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]
    authentication_classes = SessionAuthentication, BasicAuthentication
    serializer_class = BookSerializer
    queryset = Book.objects.all()
class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]
    authentication_classes = SessionAuthentication, BasicAuthentication


class AuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()