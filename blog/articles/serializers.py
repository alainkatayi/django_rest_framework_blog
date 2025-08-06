from .models import Article
from rest_framework import serializers
from accounts.serializers import UserPublicSerializer

class ArticleSerializer(serializers.ModelSerializer):
    title=  serializers.CharField(required=True)
    introduction = serializers.CharField(required=True)
    content =serializers.CharField(required=True)
    created_by = UserPublicSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y",read_only=True)
    class Meta:
        model = Article
        fields = ['id','title','introduction','content','created_at', 'created_by']
        read_only_fields = ['created_by','created_at']

