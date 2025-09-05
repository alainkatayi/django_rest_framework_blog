from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Projects
from rest_framework.generics import ListAPIView

# Create your views here.
class ProjectCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response({
                "Message":"Project create",
                "project": ProjectSerializer(project).data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ProjectUniqueView(APIView):
    permission_classes=[AllowAny]
    def get(self,request,pk):
        project = get_object_or_404(Projects, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

