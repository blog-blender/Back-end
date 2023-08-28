from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import blog,Follower
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer


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
