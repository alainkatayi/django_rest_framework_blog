from django.urls import path
from .views import CreateSkillView, SkillsListView

urlpatterns = [
    path('create/skill/',CreateSkillView.as_view(), name='create'),
    path('skills/',SkillsListView.as_view(), name='skills-list')
]