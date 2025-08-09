from rest_framework import serializers

from articles.models import Categories
from articles.serializers import CategorySerializer
from .models import Skills, Experiences

class SkillsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only= True)
    #Pour la lecture
    category = CategorySerializer(read_only=True)
    #pour l'ecriture
    category_id = serializers.PrimaryKeyRelatedField(queryset = Categories.objects.all(),
    source = 'category',
    write_only = True,
    required = True)

    class Meta:
        model = Skills
        fields = ['id','name','created_at','category','category_id']
        read_only_fields = ['created_at','category']

class ExperiencesSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(required= True)
    entreprise_name = serializers.CharField(required= True)
    start_date = serializers.DateField(required= True)
    end_date = serializers.DateField(required=False)
    current_job = serializers.BooleanField(required= True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Experiences
        fields = ['id','job_title','entreprise_name','start_date','end_date','current_job','description']