from django.urls import path
from .views import list_authors, BookListView , LibraryDetailView
from .views import list_books
from . import views
from .views import  LoginView, LogoutView

urlpatterns = [

    path('home/book_list/',  list_books, name="book_list" ),
    path('home/list_author/',  list_authors, name=" list_author" ),
    
    
    
    path('login/',  LoginView.as_view(template_name='registration/login.html') , name='login'),
    path('home/', views.home , name="home"),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('register/', views.register, name='register'),
]


