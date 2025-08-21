from rest_framework.urls import path
from django.urls import path
from.views import ProjectCreateView,ProjectListView

urlpatterns = [
    path('create/',ProjectCreateView.as_view(),name='create-project'),
    path('project/',ProjectListView.as_view(), name='list-project')
]