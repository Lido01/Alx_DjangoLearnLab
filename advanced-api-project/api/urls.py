from django.urls import path, include
from .views import  ListView, AuthorList, CreateView, UpdateView, AuthorCreate

urlpatterns = [

    path("author/",AuthorList.as_view(), name="author_list" ),
    path("author/create/", AuthorCreate.as_view(), name="author_create"),
    path("books/", ListView.as_view(), name="books"),
    path("books/author/",AuthorList.as_view(), name="book_author"),
    path("books/create/", CreateView.as_view(), name="book_create"),
    path("books/update/", UpdateView.as_view(), name="update_book" ),
    path("books/delete/", UpdateView.as_view(), name="delete_book" ),
]