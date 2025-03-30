from django.urls import path
from . import views  

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),

    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow_user'),

]
