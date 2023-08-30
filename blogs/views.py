from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView

)
from .models import blog,Follower,Categories,Category_associate
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer,CategoriesSerializer,BlogUpdateSerializer,UnfollowSerializer,FollowCreateSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics,status
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



## Follow and Unfollow blogs

class FollowBlog(generics.CreateAPIView):
    serializer_class = FollowCreateSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        blog_id = serializer.validated_data['blog_id']
        blog_instance = None

        try:
            blog_instance = blog.objects.get(pk=blog_id)
        except blog.DoesNotExist:
            return Response({'detail': 'Blog not found.'}, status=status.HTTP_400_BAD_REQUEST)

        user = self.request.user

        if Follower.objects.filter(user_id=user, blog_id=blog_instance).exists():
            return Response({'detail': 'You are already following this blog.'}, status=status.HTTP_400_BAD_REQUEST)

        Follower.objects.create(user_id=user, blog_id=blog_instance)
        return Response({'detail': 'You are now following this blog.'}, status=status.HTTP_201_CREATED)





class UnfollowBlog(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        blog_instance = get_object_or_404(blog, pk=kwargs['blog_id'])

        user = self.request.user


        try:
            follower = Follower.objects.get(user_id=user, blog_id=blog_instance)
        except Follower.DoesNotExist:
            return Response({'detail': 'You are not following this blog.'}, status=status.HTTP_400_BAD_REQUEST)


        follower.delete()
        return Response({'detail': 'You have unfollowed this blog.'}, status=status.HTTP_204_NO_CONTENT)
