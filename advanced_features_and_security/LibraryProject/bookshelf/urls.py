from django.urls import path
from .views import MyView


urlpatterns = [

    path("index/", MyView, name="index"),

]