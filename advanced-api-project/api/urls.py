from django.urls import path, include
from .views import BookList, AuthorList, BookCreate

urlpatterns = [
    path("books/", BookList.as_view(), name="books"),
    path("books/author/",AuthorList.as_view(), name="book_author"),
    path("books/create/", BookCreate.as_view(), name="book_create"),
]