from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Photo,Comment,blog
from .serializers import postSerializer, photoSerializer,commentSerializer
from blogs.serializers import followerSerializer
from blogs.models import Follower


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




class PostCreateView(APIView):
    def post(self, request, format=None):
        post_data = request.data.get('post_data')
        photo_data = request.data.get('photo_data')

        post_serializer = postSerializer(data=post_data)
        photo_serializer = photoSerializer(data=photo_data)

        if post_serializer.is_valid() and photo_serializer.is_valid():
            post_instance = post_serializer.save()
            photo_instance = photo_serializer.save()
            return Response(
                {
                    'post': post_serializer.data,
                    'photo': photo_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'post_errors': post_serializer.errors if post_data else None,
                'photo_errors': photo_serializer.errors if photo_data else None
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class commentListView(ListCreateAPIView):

    serializer_class = commentSerializer

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        if post_id:
            queryset = Comment.objects.filter(post_id=post_id)
        else:
            queryset = Comment.objects.all()
        return queryset


class HomeView(ListCreateAPIView):

    serializer_class = postSerializer
    def get_queryset(self):
            user_id = self.request.query_params.get('user_id')
            if user_id:
                queryset = Follower.objects.filter(user_id=user_id)
            else:
                queryset = Follower.objects.all()
            for blog in queryset:
                id = blog.blog_id
                posts = Post.objects.filter(blog_id=id)
            print(posts)
            return posts
