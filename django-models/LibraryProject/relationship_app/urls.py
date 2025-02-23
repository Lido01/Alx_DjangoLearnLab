from django.urls import path
from .views import list_authors, BookListView , LibraryDetailView
from .views import list_books


urlpatterns = [

    path('/home/book_list/',  list_books, name="book_list" ),
    path('/home/list_author/',  list_authors, name=" list_author" ),

]
