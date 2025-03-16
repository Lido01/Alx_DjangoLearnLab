from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book,Author
import json

# class TestView(TestCase):
#     def test_ListView_GET(self):
#         client = Client()
#         response = client.get(reverse("books"))
#         self.assertEqual(response.status_code, 200)


class BookViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.book = Book.objects.create(title="Test Book", author="Test Author", published_date="2010")

    def test_create_book(self):
        url = reverse('book_list')
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_year": "2010"
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], data['title'])

    def test_get_book_list(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    # def test_update_book(self):
    #     url = reverse('book_detail', args=[self.book.id])
    #     updated_data = {
    #         "title": "Updated Title",
    #         "author": "Updated Author",
    #         "published_date": "2023-01-01"
    #     }
    #     response = self.client.put(url, data=json.dumps(updated_data), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.book.refresh_from_db()
    #     self.assertEqual(self.book.title, "Updated Title")

    # def test_delete_book(self):
    #     url = reverse('book_detail', args=[self.book.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, 204)
    #     self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # def test_book_filtering(self):
    #     url = reverse('book-list') + '?author=Test Author'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     titles = [book['title'] for book in response.json()]
    #     self.assertIn('Test Book', titles)

    # def test_unauthenticated_access(self):
    #     self.client.logout()
    #     url = reverse('book-list')
    #     response = self.client.get(url)
    #     self.assertIn(response.status_code, [401, 403])  # Depending on your permission setup
