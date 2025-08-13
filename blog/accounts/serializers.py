from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class RegisterSerialize(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    class Meta:
        model =User
        fields = ['username', 'email', 'password']

    def create(self , validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password= validated_data['password']
            )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email' ]

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']
#custome de la class TokenObtainPair qui renvoi par defaut seulement: access et refresh
#on ajout un objet user, pour avoir aussi les informations du user qui se connecte
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({
            'user': {
                'id': self.user.id,
                'username': self.user.username,
                'email': self.user.email,
            }
        })
        return data

        
