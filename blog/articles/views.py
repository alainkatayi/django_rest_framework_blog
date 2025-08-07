from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ArticleSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from django.shortcuts import get_object_or_404
from .pagination import ArticlePagination
from rest_framework.filters import SearchFilter

# Create your views here.
class ArticleCreatedView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article =serializer.save(created_by=request.user)
            return Response({
                "Message": "Article crée avec succès",
                "article": ArticleSerializer(article).data},
                status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ArticleUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request,pk):
        article = get_object_or_404(Article,pk=pk)
        if article.created_by != request.user:
            return Response({
                "Message": "Vous n'avez pas le droit de modifier cette article"},
                status=status.HTTP_403_FORBIDDEN
                )
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message": "Article modifié avec succès",
                "Article": serializer.data},
                status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        article = get_object_or_404(Article,pk=pk)
        if article.created_by != request.user:
            return Response({
                "Message": "Vous n'avez pas le droit de supprimer cet article"}, status=status.HTTP_403_FORBIDDEN)

        article.delete()
        return Response({"Message":"Article supprimée"},status=status.HTTP_204_NO_CONTENT)

class ArticleList(ListAPIView):
    permission_classes = [AllowAny]
    
    # def get(self,request):
    #     articles = Article.objects.all()
    #     paginator = ArticlePagination()
    #     page = paginator.paginate_queryset(articles, request)
    #     serializer = ArticleSerializer(page,many = True)
    #     return paginator.get_paginated_response(serializer.data)

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    
    filter_backends = [SearchFilter]
    search_fields = ['title','content']

class ArticleUniqueView(APIView):
    permission_classes=[AllowAny]
    def get(self,request,pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

#view pour la création d'une category
class CategoryCreateView(APIView):
    permission_classes =[IsAuthenticated]

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response({
                "Message": "Catégory créé avec success",
                "category":CategorySerializer(category).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

