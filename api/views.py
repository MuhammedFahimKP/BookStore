from rest_framework import generics

from .serializers import BookSerializer
from store.models import Book

class BookListCreateApiView(generics.ListCreateAPIView):
    
    serializer_class =  BookSerializer
    queryset         =  Book.objects.all()
    

class BookRetriveApiView(generics.RetrieveAPIView):
    
    serializer_class = BookSerializer
    queryset         = Book.objects.all()
    lookup_field     = 'pk'
    
    
    
    