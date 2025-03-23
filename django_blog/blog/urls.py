from django.urls import path, include
from .views import (
        register,home, login,
        PostListView, PostDetailView,
        PostCreateView, PostUpdateView,
        PostDeleteView, profile,
        CommentCreateView, CommentUpdateView,
        CommentDeleteView,
        )

urlpatterns = (
    path("home/", home, name="home"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),


    #urls for the post CRUD operation
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),


    #urls for the Comment CRUD operation
    path('post/<int:post_id>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),


)


#def login(request):
