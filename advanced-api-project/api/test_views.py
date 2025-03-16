from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.book = Book.objects.create(title="Test Book", publication_year="2010")

    def test_create_book(self):
        url = reverse('book_list')
        data = {
            "title": "New Book",
            #"author": "New Author",
            "publication_year": "2010"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    # def test_get_book_list(self):
    #     url = reverse('book_list')
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertGreaterEqual(len(response.data), 1)

    # def test_update_book(self):
    #     url = reverse('book-detail', args=[self.book.id])
    #     updated_data = {
    #         "title": "Updated Title",
    #         "author": "Updated Author",
    #         "published_date": "2023-01-01"
    #     }
    #     response = self.client.put(url, updated_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.book.refresh_from_db()
    #     self.assertEqual(self.book.title, "Updated Title")

    # def test_delete_book(self):
    #     url = reverse('book-detail', args=[self.book.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # def test_book_filtering(self):
    #     url = reverse('book-list') + '?author=Test Author'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('Test Book', [book['title'] for book in response.data])

    # def test_unauthenticated_access(self):
    #     self.client.logout()
    #     url = reverse('book-list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)