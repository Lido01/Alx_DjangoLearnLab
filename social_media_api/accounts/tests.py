from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowSystemTest(TestCase):

    def setUp(self):
        # Create test users for the follow system
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.user3 = User.objects.create_user(username='user3', password='password123')

    def test_follow_user(self):
        # Test if a user can successfully follow another user
        self.client.login(username='user1', password='password123')  # Log in as user1
        response = self.client.post(f'/follow/{self.user2.id}/')  # Send POST request to follow user2
        self.assertEqual(response.status_code, 200)  # Ensure the response status is 200 (success)
        self.assertIn(self.user2, self.user1.following.all())  # Check that user2 is now in user1's following list

    def test_unfollow_user(self):
        # Test if a user can successfully unfollow another user
        self.user1.following.add(self.user2)  # Add user2 to user1's following list
        self.client.login(username='user1', password='password123')  # Log in as user1
        response = self.client.post(f'/unfollow/{self.user2.id}/')  # Send POST request to unfollow user2
        self.assertEqual(response.status_code, 200)  # Ensure the response status is 200 (success)
        self.assertNotIn(self.user2, self.user1.following.all())  # Check that user2 is no longer in user1's following list