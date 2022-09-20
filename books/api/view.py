from ast import arg
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from books.models import Book, Comment

from books.api.serializers import BookSerializer,  CommentSerializer


class BooksCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Book.objects.all()
    serializer_class =  BookSerializer


class CommentCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        book =  get_object_or_404(Book, pk=book_pk)
        serializer.save(book=book) 

class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Comment.objects.all()
    serializer_class =  CommentSerializer


   










# class BooksCreateApiView(ListModelMixin,  CreateModelMixin,  GenericAPIView):
#     queryset =  Book.objects.all()
#     serializer_class =  BookSerializer

#     #list
#     # listelemek
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # yaratmak istiyorum
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class CommentCreateApiView(ListModelMixin, CreateModelMixin,  GenericAPIView):
#     queryset =  Comment.objects.all()
#     serializer_class  =  CommentSerializer

#     def get(self, request,  *args, **kwargs):
#         return self.list(request, *args,  **kwargs)

#     def post(self, request,  *args,  **kwargs):
#         return self.create(request, *args, **kwargs)    

