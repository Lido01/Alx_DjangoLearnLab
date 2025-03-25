from django.urls import path, include
from .views import (
        HomeView, register, login,
        PostListView, PostDetailView,
        PostCreateView, PostUpdateView,
        PostDeleteView, profile,
        CommentCreateView, CommentUpdateView,
        CommentDeleteView, SearchView,
        PostByTagListView,
        )

urlpatterns = (
    path("home/", HomeView.as_view(), name="home"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),


    #urls for the post CRUD operation
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    #path('post/<int:pk>/comments/new/', PostCreateView.as_view(), name='post_create'),
    path('post/comments/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),


    #urls for the Comment CRUD operation
    path('post/<int:post_id>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('post/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    #Search Result show url
    path("post/search/", SearchView.as_view(), name="search" ),
    #path('tags/<str:tag_name>/', PostByTagListView.as_view(), name='posts_by_tag'),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="post_by_tag"),
     

)

#def login(request):
