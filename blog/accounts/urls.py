from django.urls import path
from .views import RegisterView
from .views import UserList

urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserList.as_view(), name='user')
]