from django.test import TestCase
from app import models

# Create your tests here.
class TestBook(TestCase):
    def test_create_book(self):
        book = models.create_book(
            "Book1",
            "Author1",
            25
        )
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Book1")
        self.assertEqual(book.num_pages, 25)

    def test_view_all(self):
        books_data = [
            {
                "title": "Book1",
                "author": "Author1",
                "num_pages": 400,
            },
            {
                "title": "Book2",
                "author": "Author2",
                "num_pages": 300,
            },
            {
                "title": "Book3",
                "author": "Author3",
                "num_pages": 200,
            }
        ]

        for book_data in books_data:
            models.create_book(
                book_data["title"],
                book_data["author"],
                book_data["num_pages"],
            )

        books = models.view_all()

        self.assertEqual(len(books), len(books_data))

        books_data = sorted(books_data, key=lambda c: c["title"])
        books = sorted(books, key=lambda c: c.title)

        for data, book in zip(books_data, books):
            self.assertEqual(data["title"], book.title)
            self.assertEqual(data["author"], book.author)
            self.assertEqual(data["num_pages"], book.num_pages)

    def test_view_by_author(self):
        books_data = [
                {
                    "title": "Elias",
                    "author": "Author1",
                    "num_pages": 400,
                },
                {
                    "title": "Martin",
                    "author": "Author2",
                    "num_pages": 300,
                },
                {
                    "title": "Alma",
                    "author": "Author1",
                    "num_pages": 200,
                }
        ]

        for book_data in books_data:
            models.create_book(
                book_data["title"],
                book_data["author"],
                book_data["num_pages"],
            )

        self.assertEqual(len(models.view_by_author("Author1")), 2)

    def test_view_by_num_pages(self):
        books_data = [
                {
                    "title": "Elias",
                    "author": "Author1",
                    "num_pages": 400,
                },
                {
                    "title": "Martin",
                    "author": "Author2",
                    "num_pages": 300,
                },
                {
                    "title": "Alma",
                    "author": "Author1",
                    "num_pages": 200,
                }
        ]

        for book_data in books_data:
            models.create_book(
                book_data["title"],
                book_data["author"],
                book_data["num_pages"],
            )

        self.assertEqual(len(models.view_by_num_pages(200)), 1)


    def test_update_author(self):
        book1 = models.create_book("book1", "author1", 400)
        book2 = models.create_book("book2", "author2", 300)
        
        models.update_author("book1", "author3")
        

        self.assertEqual(models.view_by_title("book1").author, "author3")

    def test_delete(self):
        books_data = [
            {
                "title": "Elias",
                "author": "Author1",
                "num_pages": 400,
            },
            {
                "title": "Martin",
                "author": "Author2",
                "num_pages": 300,
            },
            {
                "title": "Alma",
                "author": "Author3",
                "num_pages": 200,
            },
        ]

        for book_data in books_data:
            models.create_book(
                book_data["title"],
                book_data["author"],
                book_data["num_pages"],
            )

        models.delete("Martin")

        self.assertEqual(len(models.view_all()), 2)