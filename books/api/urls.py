from django.urls import path
from books.api import view as api_views
urlpatterns = [
   path( 'books/', api_views.BooksCreateApiView.as_view(), name='book-list'),
   path('books/<int:pk>',  api_views.BookDetailApiView.as_view(),  name='book-imformation'),
   path('books/<int:book_pk>/comment', api_views.CommentCreateApiView.as_view(), name='commet-create'),
   path( 'comments/<int:pk>', api_views.CommentDetailApiView.as_view(), name='comment-detail'),

]