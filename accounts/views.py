
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,ListAPIView
)
from rest_framework import generics
from accounts.models import CustomUser
from .serializers import UserRegistrationSerializer,userSerializer
from rest_framework.permissions import AllowAny


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()

class usersListView(ListAPIView):
    serializer_class = userSerializer
    queryset = CustomUser.objects.all()
    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            queryset = CustomUser.objects.filter(username=username)
        else:
            queryset = CustomUser.objects.all()
        return queryset

class UserUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = userSerializer
    # permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
