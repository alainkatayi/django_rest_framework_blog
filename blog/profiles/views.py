from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import SkillsSerializer, ExperiencesSerializer,CertificationsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Skills, Experiences, Certifications
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
    
class SkillUniqueView(APIView):
    permission_classes=[AllowAny]
    def get(self,request,pk):
        skill = get_object_or_404(Skills, pk=pk)
        serializer = SkillsSerializer(skill)
        return Response(serializer.data)
    
class SkillsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class SkillDeletedView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        skill = get_object_or_404(Skills, pk =pk)
        skill.delete()
        return Response({"Message": "Skill deleted "}, status=status.HTTP_204_NO_CONTENT)
    
class CreateExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        experience_serializer = ExperiencesSerializer(data= request.data)
        if experience_serializer.is_valid():
            experience= experience_serializer.save()
            return Response({
                "Message":"Experience Crated",
                "Experience":ExperiencesSerializer(experience).data
            },status = status.HTTP_201_CREATED)
        return Response(experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self,request, pk):
        experience = get_object_or_404(Experiences,pk=pk)
        experience_serializer = ExperiencesSerializer(experience, data= request.data)
        if experience_serializer.is_valid():
            experience_serializer.save()
            return Response({
                "Message":"Experience update",
                "Experience": experience_serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExperienceUniqueView(APIView):
    permission_classes=[AllowAny]
    def get(self,request,pk):
        experience = get_object_or_404(Experiences, pk=pk)
        serializer = ExperiencesSerializer(experience)
        return Response(serializer.data)
    
class DeleteExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,pk):
        experience = get_object_or_404(Experiences,pk=pk)
        experience.delete()
        return Response({"Message":"Experience Delete"}, status=status.HTTP_204_NO_CONTENT)
    
class ListExperienceView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Experiences.objects.all()
    serializer_class = ExperiencesSerializer

class CreateCertificationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        certification_serializer = CertificationsSerializer(data=request.data)
        if certification_serializer.is_valid():
            certification = certification_serializer.save()
            return Response({"Message":"certication create", "Certification": CertificationsSerializer(certification).data},status= status.HTTP_201_CREATED)
        return Response(certification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateCerticationView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        certification = get_object_or_404(Certifications,pk=pk)
        certification_serializer = CertificationsSerializer(certification,data =request.data)
        if certification_serializer.is_valid():
            certification_serializer.save()
            return Response({"Message":"Certification Update", "Certification":certification_serializer.data},status=status.HTTP_201_CREATED)
        return Response(certification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificationUniqueView(APIView):
    permission_classes=[AllowAny]
    def get(self,request,pk):
        certification = get_object_or_404(Certifications, pk=pk)
        serializer = CertificationsSerializer(certification)
        return Response(serializer.data)
    
class DeleteCertificationView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request,pk):
        certfication = get_object_or_404(Certifications,pk=pk)
        certfication.delete()
        return Response({"Message":"Certification Delete"}, status=status.HTTP_204_NO_CONTENT)
    
class ListCertificationsView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Certifications.objects.all()
    serializer_class = CertificationsSerializer