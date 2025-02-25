from django.urls import path
from .views import list_authors, BookListView , LibraryDetailView
from .views import list_books
from . import views


urlpatterns = [

    path('home/book_list/',  list_books, name="book_list" ),
    path('home/list_author/',  list_authors, name=" list_author" ),
    

    path('register/', views.RegisterView, name='register'),
    path('login/',  views.LoginView , name='login'),
    path("home/", views.home, name="home"),
    path("logout/", views.LogoutView, name="logout")
]
