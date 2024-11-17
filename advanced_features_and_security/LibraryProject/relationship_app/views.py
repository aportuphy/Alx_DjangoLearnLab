from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from relationship_app.models import Book
from .forms import BookForm

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

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()  # Create an empty form instance

    return render(request, 'relationship_app/register.html', {'form': form})

# Login View (Django's built-in)
class MyLoginView(LoginView):
    template_name = 'registration/login.html'

# Logout View (Django's built-in)
class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'

# Utility function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Utility function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Utility function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - accessible only to Admins
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin page!")

# Librarian view - accessible only to Librarians
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian page!")

# Member view - accessible only to Members
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to the Member page!")


# Add Book - Only accessible to users with the 'can_add_book' permission
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to the list of books (assuming you have that URL)
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
    # Logic to change a book
    return render(request, 'change_book.html')

# Edit Book - Only accessible to users with the 'can_change_book' permission
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to the list of books
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# Delete Book - Only accessible to users with the 'can_delete_book' permission
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')  # Redirect to the list of books
    return render(request, 'relationship_app/delete_book.html', {'book': book})

    from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Logic for adding book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic for editing book
    pass
