from django.urls import path, include
from .views import BookList

urlpatterns = [
    path("books/", BookList.as_view(), name="books")
]