from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import blog
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer


class blogList(ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer


class blogDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = blog.objects.all()
    serializer_class = blogSerializer
