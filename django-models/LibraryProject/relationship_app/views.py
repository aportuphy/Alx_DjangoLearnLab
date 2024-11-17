from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from .forms import UserLoginForm, UserRegisterForm

# Function-based view for listing books
def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Correct template path
    context_object_name = 'library'

# Authentication views (login, register)
def login_view(request):
    # Implement login logic here
    pass

def logout_view(request):
    # Implement logout logic here
    pass

def register_view(request):
    # Implement registration logic here
    pass
