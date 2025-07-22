from django.urls import path
from .views import ArticleCreatedView, ArticleList,ArticleUpdateView, ArticleDeleteView,ArticleUniqueView
urlpatterns = [
    path('create/',ArticleCreatedView.as_view(), name='create' ),#http://127.0.0.1:8000/api/article/create/
    path('list/',ArticleList.as_view(), name='listArticle' ), #http://127.0.0.1:8000/api/article/list/
    path('<int:pk>/update/',ArticleUpdateView.as_view(), name='article-update'), #http://127.0.0.1:8000/api/article/1/update/
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='delete_article'), #http://127.0.0.1:8000/api/article/1/delete/
    path('<int:pk>/',ArticleUniqueView.as_view(), name='unique') #http://127.0.0.1:8000/api/article/1
]