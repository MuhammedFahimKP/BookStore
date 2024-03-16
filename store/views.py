from django.views import View,generic
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
import sweetify
from .forms import BookCreationForm
from .models import Book


# Create your views here.



class BookListView(View):
    
    def get(self,request):
        
        books = Book.objects.all()
        context = {
            'books': books
        }
        return render(request,'home.html',context)
    
class BookRetriveView(View):
    
    def get(self,request,pk):
        
        book = Book.objects.filter(id=pk)
        
        if not book:
            return redirect('book-list-view')
        
        
        book = book[0]
        
        context = {
            'book':book
        }
        
        return render(request,'singlebook.html',context)


class BookCreateView(generic.CreateView):

    form_class = BookCreationForm
    model = Book 
    template_name = 'createbook.html'
    success_url = reverse_lazy('addprd')

    def form_valid(self, form):
        sweetify.sweetalert(self.request,icon="success",text=f"Book added",title="Done",timer='3000',position='top-end',toast=True)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        sweetify.sweetalert(self.request,icon="error",text=f"failed to add book",title="failed",timer='3000',position='top-end',toast=True)
        return super().form_invalid(form)
    
    



