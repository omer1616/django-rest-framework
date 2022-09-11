from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_api_view
from news.api import views as api_views


urlpatterns = [
    path('articles/', api_views.ArticleListCreateAPIView.as_view(), name='articles'),
    path('articles/<int:pk>/', api_views.ArticleDetailAPIView.as_view(), name='articles-detail'),
]

## function method
# urlpatterns = [
#     path('articles/', article_list_create_api_view, name='articles'),
#      path('articles/<int:pk>/', article_detail_api_view, name='articles-detail'),
# ]