from rest_framework.urls import path
from django.urls import path
from.views import ProjectCreateView

urlpatterns = [
    path('create/',ProjectCreateView.as_view(),name='create-project'),
]