from django.shortcuts import render
from django.views import View
from relationship_app.models import Book, Library

# Function-based View for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based View for displaying a specific library's details
class LibraryDetailView(View):
    def get(self, request, library_name):
        library = Library.objects.get(name=library_name)
        return render(request, 'library_detail.html', {'library': library})
