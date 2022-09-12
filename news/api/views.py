from typing import Tuple
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from news.models import Article,  Journalist
from .serializers import ArticleSerializer, JournalistSerializer




class JournalistListCreateAPIView(APIView):
    def get(self, request):
        journalist =  Journalist.objects.all()
        serializer =  JournalistSerializer(journalist, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer =  JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,   status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListCreateAPIView(APIView):
    def get(self, request):
        article = Article.objects.filter(status=True)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = Article(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
