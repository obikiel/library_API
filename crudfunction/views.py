from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class BookList(APIView):
    """
    List all books or create a new book.
    """
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({
            "status": "success",
            "code": 200,
            "message": "Books retrieved successfully",
            "data": {"books": serializer.data}
        })

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "code": 201,
                "message": "Book added successfully",
                "data": {"book": serializer.data}
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "code": 400,
            "message": "Invalid data",
            "errors": serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    """
    Retrieve, update, or delete a book by id.
    """
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        serializer = BookSerializer(book)
        return Response({
            "status": "success",
            "code": 200,
            "message": "Book details retrieved successfully",
            "data": {"book": serializer.data}
        })

    def put(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "code": 200,
                "message": "Book updated successfully",
                "data": {"book": serializer.data}
            })
        return Response({
            "status": "error",
            "code": 400,
            "message": "Invalid data",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return Response({
            "status": "success",
            "code": 204,
            "message": "Book deleted successfully",
            "data": {}
        }, status=status.HTTP_204_NO_CONTENT)