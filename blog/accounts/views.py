from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import RegisterSerialize,UserSerializer,CustomTokenObtainPairSerializer
from rest_framework import status 
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, Request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
