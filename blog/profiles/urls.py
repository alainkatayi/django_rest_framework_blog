from django.urls import path
from .views import CreateSkillView, SkillsListView,SkillUpdateView,SkillDeletedView

urlpatterns = [
    path('create/skill/',CreateSkillView.as_view(), name='create'),
    path('skills/',SkillsListView.as_view(), name='skills-list'),
    path('<int:pk>/update/',SkillUpdateView.as_view(), name='update-skill'),
    path('<int:pk>/delete/',SkillDeletedView.as_view(), name='delete-skill'),
]