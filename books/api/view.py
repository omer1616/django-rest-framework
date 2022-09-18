from ast import arg
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from books.models import Book, Comment

from books.api.serializers import BookSerializer,  CommentSerializer


class BooksCreateApiView(ListModelMixin,  CreateModelMixin,  GenericAPIView):
    queryset =  Book.objects.all()
    serializer_class =  BookSerializer

    #list
    # listelemek
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # yaratmak istiyorum
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentCreateApiView(ListModelMixin, CreateModelMixin,  GenericAPIView):
    queryset =  Comment.objects.all()
    serializer_class  =  CommentSerializer

    def get(self, request,  *args, **kwargs):
        return self.list(request, *args,  **kwargs)

    def post(self, request,  *args,  **kwargs):
        return self.create(request, *args, **kwargs)    

