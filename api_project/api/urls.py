from django.urls import path, include
from .views import BookList,BookCreate, BookViewSet
#from django.views import  
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [

    path("books/", BookList.as_view(), name="book-list"),
    path("books_create/", BookCreate.as_view(), name="book-create"),
    path("obtain_token/", obtain_auth_token, name="obtain_token"),
    path('viewset/', include(router.urls)), #THis includes all routes registered with the router

]