from django.urls import path
from books.api import view as api_views
urlpatterns = [
   path( 'books/', api_views.BooksCreateApiView.as_view(), name='book-list'),
   path( 'comments/', api_views.CommentCreateApiView.as_view(), name='comment-list'),

]