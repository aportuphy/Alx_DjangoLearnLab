from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

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
