from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<str:library_name>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
