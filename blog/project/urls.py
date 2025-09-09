from rest_framework.urls import path
from django.urls import path
from.views import DeleteProjectView, ProjectCreateView,ProjectListView,ProjectUniqueView, UpdateProjectView

urlpatterns = [
    path('create/',ProjectCreateView.as_view(),name='create-project'),
    path('project/',ProjectListView.as_view(), name='list-project'),
    path('<int:pk>/',ProjectUniqueView.as_view(), name='unique-project'),
    path('<int:pk>/delete/',DeleteProjectView.as_view(), name='delete-project'),
    path('<int:pk>/update/',UpdateProjectView.as_view(), name='update-project'),
]