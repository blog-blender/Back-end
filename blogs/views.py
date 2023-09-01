from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
    DestroyAPIView
)
from .models import blog,Follower,Categories,Category_associate
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer,CategoriesSerializer,Category_associateSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import difflib
from rest_framework import status
from .serializers import BlogUpdateSerializer,FollowCreateSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def blogList(request):
    if request.method == 'GET':
        owner = request.query_params.get('owner')
        blog_id = request.query_params.get('blog_id')
        if owner:
            blogs = blog.objects.filter(owner=owner)
        elif blog_id:
            blogs = blog.objects.filter(id=blog_id)
        else:
            blogs = blog.objects.all()
    return blog_getter(request, blogs)

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

@api_view(['GET'])
def searchView(request):
    if request.method == 'GET':
        catigory = request.query_params.get('catigory')
        blog_title = request.query_params.get('blog_title')
        if catigory and blog_title:
            blogs = Category_associate.objects.filter(category_name=catigory)
            blogs_lsit=[]
            for b in blogs:
                blogs_data = Category_associateSerializer(b, context={'request': request}).data
                blogs_lsit.append(blogs_data)
        blogs = blog.objects.all()
        def matching(blogs_list, blog_title):
            best_ratio = 0.65
            best_response = []
            if blog_title and catigory :
                for i in blogs_list:
                    ratio = difflib.SequenceMatcher(None, i["catigory"]["title"], blog_title).ratio()
                    if ratio > best_ratio:
                        best_ratio = ratio
                        best_response.append(i)
            if blog_title :
                for i in blogs_list:
                    ratio = difflib.SequenceMatcher(None, i["title"], blog_title).ratio()
                    if ratio > best_ratio:
                        best_ratio = ratio
                        best_response.append(i)
            elif catigory :
                    for i in blogs_list:
                        ratio = difflib.SequenceMatcher(None, i["catigory"], blog_title).ratio()
                        if ratio > best_ratio:
                            best_ratio = ratio
                            best_response.append(i)
            if best_ratio > 0.65:
                return best_response
            else:
                return blogs_list
        if catigory:
            blogs = Category_associate.objects.filter(category_name=catigory)
            blogs_lsit=[]
            for b in blogs:
                blogs_data = Category_associateSerializer(b, context={'request': request}).data
                blogs_lsit.append(blogs_data)
            return Response(blogs_lsit)
        blogs_lsit=[]
        for b in blogs:
            blogs_data = blogSerializer(b, context={'request': request}).data
            blogs_lsit.append(blogs_data)
        return Response(matching(blogs_lsit,blog_title))

class CreateBlog(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        serializer = blogSerializer(data=request.data)
        category = request.data['category']
        if serializer.is_valid():
            serializer.save(owner=request.user)
            created_blog = serializer.instance  # Get the created blog instance
            created_blog_id = created_blog.id
            print(type(created_blog_id))
            data = {'category_name': category, 'blog_id': created_blog_id}
            print(data)
            s = Category_associateSerializer(data=data)
            if s.is_valid():
                s.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = blog.objects.all()
    serializer_class = BlogUpdateSerializer
    lookup_url_kwarg = 'blog_id'

class FollowBlog(CreateAPIView):
    serializer_class = FollowCreateSerializer

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

class UnfollowBlog(DestroyAPIView):
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


########################## sevices ###########################
def blog_getter(request, blogs):
    blog_list = []
    for b in blogs:
        blog_data = blogSerializer(b, context={'request': request}).data
        Category_associates = Category_associate.objects.filter( blog_id= b.id)
        if Category_associates:
            Category_associateslist = []
            for a in Category_associates:
                Category_associates_data = Category_associateSerializer(a, context={'request': request}).data
                Category_associateslist.append(Category_associates_data)
                blog_data['Category_associates'] = Category_associateslist
        else:
            blog_data['Category_associates'] = []
        blog_list.append(blog_data)
    return Response(blog_list)
