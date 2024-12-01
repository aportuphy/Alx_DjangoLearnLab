from django.db import models

# Create your models here.

# Author model representing authors of books
class Author(models.Model):
    name = models.CharField(max_length=255)  # Field for author's name

    def __str__(self):
        return self.name

# Book model representing books written by authors
class Book(models.Model):
    title = models.CharField(max_length=255)  # Field for book title
    publication_year = models.IntegerField()  # Field for year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Foreign key linking to Author

    def __str__(self):
        return self.title
