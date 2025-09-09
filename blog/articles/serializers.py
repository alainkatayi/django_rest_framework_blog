from .models import Article, Categories
from rest_framework import serializers
from accounts.serializers import UserPublicSerializer

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(format="%d/%m/%y", read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name','description','created_at']
        read_only_fields = ['created_at']

class ArticleSerializer(serializers.ModelSerializer):
    title=  serializers.CharField(required=True)
    #affiche l'objet Categories
    category = CategorySerializer(read_only=True)
    #passe l'id de la categories
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Categories.objects.all(),
        source='category',
        write_only=True,
        required=True
    )
    introduction = serializers.CharField(required=True)
    content =serializers.CharField(required=True)
    created_by = UserPublicSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y",read_only=True)
    image = serializers.ImageField()
    class Meta:
        model = Article
        fields = ['id','title','introduction','content','created_at', 'created_by','category','category_id','image']
        read_only_fields = ['created_by','created_at','category']
