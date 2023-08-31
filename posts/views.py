from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Photo,Comment
from .serializers import postSerializer, photoSerializer,commentSerializer,CommentSerializer,PostUpdateSerializer
from .models import Post, Photo,Comment,Like
from .serializers import postSerializer, photoSerializer,commentSerializer,LikeSerializer
from blogs.models import Follower
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET'])
def postDetail(request):
    if request.method == 'GET':
        post_id = request.query_params.get('post_id')
        post = Post.objects.filter(id=post_id)
        post_data = postSerializer(post[0], context={'request': request}).data
        comments = Comment.objects.filter( post_id= post_id)
        if comments:
            comment_list = []
            for c in comments:
                comment_data = commentSerializer(c, context={'request': request}).data
                comment_list.append(comment_data)
            post_data['comments'] = comment_list
        photo = Photo.objects.filter(post_id=post_id)
        if photo:
            photos_list = []
            for p in photo:
                photo_data=photoSerializer(p, context={'request': request}).data
                photos_list.append(photo_data)
            post_data['photo'] = photos_list
        likes = Like.objects.filter(post_id=post_id)
        if likes:
            likes_list = []
            for l in likes :
                like_data=LikeSerializer(l, context={'request': request}).data
                likes_list.append(like_data)
            post_data['likes'] = len(likes_list)
        return Response(post_data)

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
            post_serializer.save()
            photo_serializer.save()
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

class CreatePost(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        serializer = postSerializer(data=request.data)
        photos = request.data.get('photos', [])
        if serializer.is_valid():
            post_instance = serializer.save()
            created_post_id = post_instance.id
            photo_data_list = [{'post_id': created_post_id, 'data': photo} for photo in photos]
            photo_serializer = photoSerializer(data=photo_data_list, many=True)
            if photo_serializer.is_valid():
                photo_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecentPosts(ListCreateAPIView):
    serializer_class = postSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Post.objects.filter(Auther_id_id=user_id)
        return queryset

class commentListView(ListCreateAPIView):
    serializer_class = commentSerializer
    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        if post_id:
            queryset = Comment.objects.filter(post_id=post_id)
        else:
            queryset = Comment.objects.all()
        return queryset

def get_queryset(request):
        user_id = request.query_params.get('user_id')
        num_of_posts = request.query_params.get('num_of_posts')
        if user_id:
            queryset = Follower.objects.filter(user_id=user_id)
        else:
            queryset = Follower.objects.all()
        if not queryset:
            return []
        for blog in queryset:
            id = blog.blog_id
            posts = Post.objects.filter(blog_id=id)
        if num_of_posts:
            return posts[:int(num_of_posts)]
        return posts

@api_view(['GET'])
def homeView(request):
    if request.method == 'GET':
        posts = get_queryset(request)
        data = []
        if  posts==[]:
            return Response("This user doesn't follow any blogs")
        for post in posts:
            post_data = postSerializer(post, context={'request': request}).data
            comments = Comment.objects.filter(post_id=post.id)
            comment_data = commentSerializer(comments, many=True, context={'request': request}).data
            post_data['comments'] = comment_data
            data.append(post_data)
        return Response(data)

class CommentUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'

class PostUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_url_kwarg = 'post_id'




# {
#   "post_data": {
#     "title": "Sample Post Title",
#     "Auther_id": 1,  // Replace with a valid user ID
#     "content": "This is the content of the sample post.",
#     "blog_id": 1     // Replace with a valid blog ID
#   },
#   "photo_data": {
#     "data": "base64_encoded_image_data_here"
#   }
# }


