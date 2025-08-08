from django.urls import path
from .views import CreateSkillView

urlpatterns = [
    path('create/skill/',CreateSkillView.as_view(), name='create')
]