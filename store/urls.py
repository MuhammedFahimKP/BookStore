from django.urls import path
from .views import BookListView,BookRetriveView,BookCreateView

urlpatterns = [
    path('',BookListView.as_view(),name="book-list-view"),
    path('<int:pk>/',BookRetriveView.as_view() , name='book-retrive-view'),
    path('create/',BookCreateView.as_view(), name="book-create")
]