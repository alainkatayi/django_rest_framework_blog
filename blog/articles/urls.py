from django.urls import path
from .views import ArticleCreatedView, ArticleList
urlpatterns = [
    path('create/',ArticleCreatedView.as_view(), name='create' ),
    path('list/',ArticleList.as_view(), name='listArticle' )
]