from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    num_pages = models.IntegerField()

def create_book(title, author, num_pages):
    book = Book(title=title, author=author, num_pages=num_pages)
    book.save()
    return book

def view_all():
    return Book.objects.all()

def view_by_author(author):
    return Book.objects.filter(author=author)

def view_by_num_pages(num_pages):
    return Book.objects.filter(num_pages=num_pages)

def update_author(title, new_author):
    b = view_by_title(title)
    b.author = new_author
    b.save()

def delete(title):
    book = Book.objects.filter(title=title)
    book.delete()

def view_by_title(title):
    book = Book.objects.get(title=title)
    return book


