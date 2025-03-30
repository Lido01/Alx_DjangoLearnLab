from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class FeedTest(TestCase):

    def setUp(self):
        # Create test users and posts for the feed functionality
        self.user1 = User.objects.create_user(username='user1', password='password123')  # The main user
        self.user2 = User.objects.create_user(username='user2', password='password123')  # A user to follow
        self.post1 = Post.objects.create(user=self.user2, content='Hello World!')  # A post by user2
        self.post2 = Post.objects.create(user=self.user2, content='Another Post!')  # Another post by user2

    def test_feed_shows_followed_user_posts(self):
        # Test if the feed shows posts from followed users
        self.user1.following.add(self.user2)  # user1 follows user2
        self.client.login(username='user1', password='password123')  # Log in as user1
        response = self.client.get('/feed/')  # Send GET request to fetch the feed
        self.assertEqual(response.status_code, 200)  # Ensure the response status is 200 (success)
        self.assertContains(response, 'Hello World!')  # Check that user2's post appears in the feed
        self.assertContains(response, 'Another Post!')  # Check that all posts by user2 appear in the feed

    def test_feed_excludes_non_followed_user_posts(self):
        # Test if the feed excludes posts from users who are not followed
        self.client.login(username='user1', password='password123')  # Log in as user1
        response = self.client.get('/feed/')  # Send GET request to fetch the feed
        self.assertEqual(response.status_code, 200)  # Ensure the response status is 200 (success)
        self.assertNotContains(response, 'Hello World!')  # Check that posts from user2 are not included
        self.assertNotContains(response, 'Another Post!')  # Ensure all posts from unfollowed users are excluded