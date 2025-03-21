from django.urls import path, include
from .views import register, home, login, PostView

urlpatterns = {
    path("home/",  home, name="home"),
    path("register/", register, name="register"),
    path("post/", PostView.as_view(), name="post"),
    path("login/", login, name="login"),
    # path(""),

}


#def login(request):
