from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationAPIView,usersListView

# from .views import SignUpView

urlpatterns = [
    # path("signup/", SignUpView.as_view(), name="signup"),
    path('/register', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('/users', usersListView.as_view(), name='user-list'),
]
