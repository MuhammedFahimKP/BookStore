from django.urls import path
from .views import BookListCreateApiView,BookRetriveApiView


urlpatterns = [
    path('',BookListCreateApiView.as_view(),name="book-list-create"),   
    path('book/<int:pk>/',BookRetriveApiView.as_view(),name="book-retrive")
]
