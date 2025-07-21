from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from django.shortcuts import get_object_or_404

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
        return Response(serializer.erro,status=status.HTTP_400_BAD_REQUEST)
    
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

class ArticleList(APIView):
    permission_classes = [AllowAny]
    
    def get(self, Request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)