from django.contrib import admin
from django.urls import path
from .views import BookList, BookDetail


urlpatterns = [
    path('api/v1/books/', BookList.as_view(), name='book-list'),
    path('api/v1/books/<int:book_id>/', BookDetail.as_view(), name='book-detail'),
]