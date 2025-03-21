from django.urls import path, include
from .views import (
        register,home, login,
        ListView, DetailView,
        CreateView, UpdateView,
        DeleteView, profile
        )

urlpatterns = (
    path("home/", home, name="home"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path("post/", ListView.as_view(), name="post"),
    path("login/", login, name="login"),


    #urls for the post CRUD operation
    path('post/', ListView.as_view(), name='post_list'),
    path('post/<int:pk>/', DetailView.as_view(), name='post_detail'),
    path('post/new/', CreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post_delete'),

)


#def login(request):
