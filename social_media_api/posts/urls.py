from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts_all', PostViewSet, basename='posts_all')

urlpatterns = [
    #path("post/", PostViewSet, name="posts"),
    path('postviewset/', include(router.urls)), #THis includes all routes registered with the router
]
