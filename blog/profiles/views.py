from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import SkillsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Skills

# Create your views here.
class CreateSkillView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SkillsSerializer(data = request.data)
        if serializer.is_valid():
            skill = serializer.save()
            return Response({
                "Message": "Skill create with success",
                "skill": SkillsSerializer(skill).data
            },status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    