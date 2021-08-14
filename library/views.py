from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
