from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()

        # Authenticate the client
        self.client.login(username="testuser", password="testpassword")

        # Create sample data
        self.author = Author.objects.create(name="Jane Doe")
        self.book = Book.objects.create(title="Sample Book", publication_year=2023, author=self.author)

    def test_create_book(self):
        """Test creating a new book."""
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id,
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_get_book_list(self):
        """Test retrieving the list of books."""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Sample Book")

    def test_update_book(self):
        """Test updating an existing book."""
        data = {"title": "Updated Book"}
        response = self.client.put(f"/api/books/{self.book.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(f"/api/books/{self.book.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """Test filtering books by title."""
        response = self.client.get("/api/books/?title=Sample Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get("/api/books/?search=Sample")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication year."""
        Book.objects.create(title="Another Book", publication_year=2021, author=self.author)
        response = self.client.get("/api/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Another Book")
