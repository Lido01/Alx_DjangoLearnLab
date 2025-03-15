from django.urls import path, include
from .views import  ListView, AuthorList, CreateView

urlpatterns = [
    path("books/", ListView.as_view(), name="books"),
    path("books/author/",AuthorList.as_view(), name="book_author"),
    path("books/create/", CreateView.as_view(), name="book_create"),
]