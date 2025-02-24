from django.urls import path
from .views import list_authors, BookListView , LibraryDetailView
from .views import list_books
from . import views


urlpatterns = [

    path('home/book_list/',  list_books, name="book_list" ),
    path('home/list_author/',  list_authors, name=" list_author" ),
    

    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/',  views.Login.as_view(template_name='templates/login.html'), name='login'),
    
]
