from django.urls import path
from .views import ArticleCreatedView, ArticleList,ArticleUpdateView
urlpatterns = [
    path('create/',ArticleCreatedView.as_view(), name='create' ),
    path('list/',ArticleList.as_view(), name='listArticle' ),
    path('<int:pk>/update/',ArticleUpdateView.as_view(), name='article-update'),
]