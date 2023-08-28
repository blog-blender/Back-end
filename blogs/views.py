from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView

)
from .models import blog,Follower,Categories,Category_associate
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer,CategoriesSerializer
from rest_framework.views import APIView


class blogList(ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer


class blogDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = blog.objects.all()
    serializer_class = blogSerializer

class followerList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Follower.objects.all()
    serializer_class = followerSerializer


class Category_list(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


