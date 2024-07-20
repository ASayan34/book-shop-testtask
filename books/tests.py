from django.test import TestCase
from .models import Book


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title='Test Book', author='Test Author', year=2021)

    def test_book_creation(self):
        book = Book.objects.get(title='Test Book')
        self.assertEqual(book.author, 'Test Author')

    def test_book_deletion(self):
        book = Book.objects.get(title='Test Book')
        book.delete()
        self.assertFalse(Book.objects.filter(title='Test Book').exists())

    def test_book_search(self):
        books = Book.objects.filter(author='Test Author')
        self.assertTrue(books.exists())

    def test_book_status_update(self):
        book = Book.objects.get(title='Test Book')
        book.status = 'borrowed'
        book.save()
        self.assertEqual(book.status, 'borrowed')
