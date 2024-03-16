from rest_framework import serializers
from store.models import Book
from .exceptions import BookAlreadyExists


class BookSerializer(serializers.ModelSerializer):
    
    
    def validate(self,data):

        book = Book.objects.filter(title__iexact=data['title'])

        if book.exists():
            raise BookAlreadyExists({'title' : 'book with same title all ready exists '})        
        
        return data
    
    class Meta:
        
        model = Book
        fields = ['id','title','author','img']
        extra_kwargs = {'id': {'read_only': True} }
        
        
        