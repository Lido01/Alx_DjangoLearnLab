from django.urls import path
from .views import list_authors, BookListView , LibraryDetailView
from .views import list_books
from . import views
from .views import  LoginView, LogoutView, add_book, admin_view, librarian_view,member_view

urlpatterns = [

    path('list_book/',  list_books, name="book_list" ),
    path('list_author/',  list_authors, name=" list_author" ),
    
    
    
    path('login/',  LoginView.as_view(template_name='relationship_app/login.html') , name='login'),
    path('home/', views.home , name="home"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path("admin/", views.admin_view, name="admin"),
    path("librarian/", views.librarian_view, name="librarian"),
    path("member/", views.member_view, name="member"),

    path("book/add/", add_book, name="book_add" ),
]


