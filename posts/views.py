from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import postSerializer


class postList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer


class postDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = postSerializer
