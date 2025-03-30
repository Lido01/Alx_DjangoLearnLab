from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
User = get_user_model()
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commnets")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who liked the post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")  # Post being liked
    timestamp = models.DateTimeField(auto_now_add=True)  # When the like happened

    def __str__(self):
        return f"{self.user} likes {self.post.title}"
