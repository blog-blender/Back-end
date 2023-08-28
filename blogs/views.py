from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,

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
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Follower.objects.all()
    serializer_class = followerSerializer





class FollowedBlogsView(ListAPIView):

    serializer_class = followerSerializer
    def get_queryset(self):
            user_id = self.request.query_params.get('user_id')
            if user_id:
                queryset = Follower.objects.filter(user_id=user_id)
            else:
                queryset = Follower.objects.all()
            return queryset
# class OwnedBlogsView(RetrieveUpdateDestroyAPIView):

#     serializer_class = followerSerializer
#     def get_queryset(self):
#             blog_id = self.request.query_params.get('blog_id')
#             if blog_id:
#                 queryset = blog.objects.filter(blog_id=blog_id)
#             else:
#                 queryset = blog.objects.all()
#             return queryset
