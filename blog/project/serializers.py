from rest_framework import serializers

from articles.serializers import CategorySerializer
from articles.models import Categories
from profiles.serializers import SkillsSerializer
from .models import Projects
from profiles.models import Skills

class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    created_at = serializers.DateField(format="%d/%m/%Y",required=True)
    category = CategorySerializer(read_only=True)
    technology_ids=serializers.PrimaryKeyRelatedField(
        many=True,
        queryset = Skills.objects.all(),
        required = True,
        write_only=True,
        source='technology'
    )
    technology=SkillsSerializer(many=True,read_only=True)
    status=serializers.BooleanField(required=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset =Categories.objects.all(),
        source='category',
        write_only = True, 
        required = True
    )
    
    class Meta:
        model = Projects
        fields = ['id','name','description','created_at', 'status','technology_ids','category_id','category','technology']
        read_only_fields=['category']