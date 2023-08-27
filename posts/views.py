from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import postSerializer
from django.http import HttpResponse
from django.views import View


# class postList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = postSerializer


class postDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = postSerializer


class postList(ListCreateAPIView):

    serializer_class = postSerializer

    def get_queryset(self):
        blog_id = self.request.query_params.get('blog_id')
        if blog_id:
            queryset = Post.objects.filter(blog_id=blog_id)
        else:
            queryset = Post.objects.all()
        return queryset





