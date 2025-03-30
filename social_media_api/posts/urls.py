from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts_all', PostViewSet, basename='posts_all')
router.register("comments", CommentViewSet, basename="comments")


urlpatterns = [
    #path("post/", PostViewSet, name="posts"),
    path('', include(router.urls)), #THis includes all routes registered with the router
    #path("commentviewset/",)

    path('feed/', FeedView.as_view(), name='feed'),

]
