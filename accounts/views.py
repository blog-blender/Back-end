
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,ListAPIView
)
from rest_framework import generics
from accounts.models import CustomUser
from .serializers import UserRegistrationSerializer,userSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response

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


############################################################################
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def UserRegistrationAPIView(request):
#     query_dict_dict = {}
#     for key, values in request.data.lists():
#         if len(values) == 1:
#             query_dict_dict[key] = values[0]
#         else:
#             query_dict_dict[key] = values

#     user_instance = UserRegistrationSerializer(data=query_dict_dict)
#     if user_instance.is_valid():
#         newuser = user_instance.save()
#     else:
#         errors = user_instance.errors
#         return Response(errors)
#     result_obj = CustomUser.objects.filter(id = f"{newuser.id}")
#     result_ser = userSerializer(result_obj[0]).data
#     print(result_obj[0])
#     return Response(result_ser)
