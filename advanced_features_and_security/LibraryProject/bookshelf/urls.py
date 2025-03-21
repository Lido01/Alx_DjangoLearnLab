from django.urls import path
from .views import MyView, edit_view


urlpatterns = [

    path("index/", MyView, name="index"),
    path("edit/", edit_view, name="edit"),

]