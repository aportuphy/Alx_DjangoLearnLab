"from bookshelf.models import Book"

book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book you want to delete
book.delete()                                          # Delete the book from the database

