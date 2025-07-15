from .models import Article
from rest_framework import serializers
from accounts.serializers import UsePublicSerialize

class ArticleSerializer(serializers.ModelSerializer):
    title=  serializers.CharField(required=True)
    content =serializers.CharField(required=True)
    created_by = UsePublicSerialize(read_only=True)
    class Meta:
        model = Article
        fields = ['id','title','content','created_at', 'created_by']
        read_only_fields = ['created_by','created_at']

