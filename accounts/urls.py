from django.urls import path
from .views import UserRegistrationAPIView,usersListView,UserUpdateView


urlpatterns = [
    path('/register', UserRegistrationAPIView, name='user-registration'),
    path('/users', usersListView.as_view(), name='user-list'),
    path('/update', UserUpdateView.as_view(), name='user-update'),
]
