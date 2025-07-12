from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerialize
from rest_framework import status 
from rest_framework.response import Response

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serialiser = RegisterSerialize(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                "Message": "Compte créé avec succès"}, status=status.HTTP_201_CREATED
                )
        return Response(serialiser.error, status=status.HTTP_400_BAD_REQUEST)
    
    
