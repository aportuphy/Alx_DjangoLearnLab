from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        serializer.save()

class BookListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
