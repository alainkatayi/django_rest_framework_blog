from django.urls import path
from .views import CreateSkillView, SkillsListView,SkillUpdateView,SkillDeletedView,CreateExperienceView,UpdateExperienceView, DeleteExperienceView, ListExperienceView,CreateCertificationView,UpdateCerticationView,DeleteCertificationView,ListCertificationsView

urlpatterns = [
    #_____skill-routes___________
    path('create/skill/',CreateSkillView.as_view(), name='create-skill'),
    path('skills/',SkillsListView.as_view(), name='skills-list'),
    path('<int:pk>/update/skill/',SkillUpdateView.as_view(), name='update-skill'),
    path('<int:pk>/delete/skill/',SkillDeletedView.as_view(), name='delete-skill'),

    #_____experience-routes_______
    path('create/experience/',CreateExperienceView.as_view(), name='create-experience'),
    path('<int:pk>/update/experience/',UpdateExperienceView.as_view(), name='update-experience'),
    path('<int:pk>/delete/experience/',DeleteExperienceView.as_view(), name='delete-experience'),
    path('experience/',ListExperienceView.as_view(), name='list-experience'),

    #______certication-routes____________
    path('create/certification/',CreateCertificationView.as_view(),name='create-certification'),
    path('<int:pk>/update/certification/',UpdateCerticationView.as_view(), name='update-certification'),
    path('<int:pk>/delete/certification/',DeleteCertificationView.as_view(), name='delete-certification'),
    path('certifications/',ListCertificationsView.as_view(), name='list-certification'),



]