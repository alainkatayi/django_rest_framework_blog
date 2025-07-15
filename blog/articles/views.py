from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Article

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

class ArticleList(APIView):
    permission_classes = [AllowAny]
    
    def get(self, Request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)