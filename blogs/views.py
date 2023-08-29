from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView

)
from .models import blog,Follower,Categories,Category_associate
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer,CategoriesSerializer,BlogUpdateSerializer
from rest_framework.views import APIView


class blogList(ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer
    def get_queryset(self):
        owner = self.request.query_params.get('owner')
        if owner:
            queryset = blog.objects.filter(owner=owner)
        else:
            queryset = blog.objects.all()
        return queryset


class blogDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = blog.objects.all()
    serializer_class = blogSerializer

class followerList(ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Follower.objects.all()
    serializer_class = followerSerializer


class Category_list(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class BlogFollowersView(ListAPIView):

    serializer_class = followerSerializer
    def get_queryset(self):
            user_id = self.request.query_params.get('user_id')
            if user_id:
                queryset = Follower.objects.filter(user_id=user_id)
            else:
                queryset = Follower.objects.all()
            return queryset


##update and delete blog
class BlogUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = blog.objects.all()
    serializer_class = BlogUpdateSerializer
    lookup_url_kwarg = 'blog_id'
