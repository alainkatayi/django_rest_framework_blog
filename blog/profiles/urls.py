from django.urls import path
from .views import CreateSkillView, SkillsListView,SkillUpdateView,SkillDeletedView,CreateExperienceView,UpdateExperienceView, DeleteExperienceView, ListExperienceView,CreateCertificationView,UpdateCerticationView,DeleteCertificationView,ListCertificationsView,CertificationUniqueView

urlpatterns = [
    #_____skill-routes___________
    path('skills/create/',CreateSkillView.as_view(), name='create-skill'),
    path('skills/',SkillsListView.as_view(), name='skills-list'),
    path('<int:pk>/skills/update/',SkillUpdateView.as_view(), name='update-skill'),
    path('<int:pk>/skills/delete/',SkillDeletedView.as_view(), name='delete-skill'),

    #_____experience-routes_______
    path('experiences/create/',CreateExperienceView.as_view(), name='create-experience'),
    path('<int:pk>/experiences/update/',UpdateExperienceView.as_view(), name='update-experience'),
    path('<int:pk>/experiences/delete/',DeleteExperienceView.as_view(), name='delete-experience'),
    path('experiences/',ListExperienceView.as_view(), name='list-experience'),

    #______certication-routes____________
    path('certification/create/',CreateCertificationView.as_view(),name='create-certification'),
    path('<int:pk>/certifications/update/',UpdateCerticationView.as_view(), name='update-certification'),
    path('<int:pk>/certification/',CertificationUniqueView.as_view(), name='unique-certification'),
    path('<int:pk>/certifications/delete/',DeleteCertificationView.as_view(), name='delete-certification'),
    path('certifications/',ListCertificationsView.as_view(), name='list-certification'),



]