from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import SkillsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Skills
from django.shortcuts import get_object_or_404

# Create your views here.
class CreateSkillView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        skill_serializer = SkillsSerializer(data = request.data)
        if skill_serializer.is_valid():
            skill = skill_serializer.save()
            return Response({
                "Message": "Skill create with success",
                "skill": SkillsSerializer(skill).data
            },status= status.HTTP_201_CREATED)
        return Response(skill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SkillUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        skill = get_object_or_404(Skills,pk=pk)
        skill_serializer = SkillsSerializer(skill,data = request.data)
        if skill_serializer.is_valid():
            skill_serializer.save()
            return Response({
                "Message":"Skill update with success",
                "skill": skill_serializer.data
            },status = status.HTTP_201_CREATED)
        return Response(skill_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class SkillsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer