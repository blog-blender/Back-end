from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView

)
from .models import blog,Follower,Categories,Category_associate
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer,CategoriesSerializer,Category_associateSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import difflib

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


def matching(blogs_lsit,blog_title):
    best_ratio = 0
    best_response = []
    for i in blogs_lsit:
        ratio = difflib.SequenceMatcher(None, i["blog_id"]["title"], blog_title).ratio()
        if ratio > best_ratio :
            best_ratio = ratio
            best_response.append(i)
    if (best_ratio >= 0.9):
        print(best_response[0])
        return best_response[0]
    else :
        return blogs_lsit #if dont find return all blogs


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
            return Response(matching(blogs_lsit,blog_title))
        if catigory:
            blogs = Category_associate.objects.filter(category_name=catigory)
            blogs_lsit=[]
            for b in blogs:
                blogs_data = Category_associateSerializer(b, context={'request': request}).data
                blogs_lsit.append(blogs_data)
            return Response(blogs_lsit)
        blogs = blog.objects.all()
        blogs_lsit=[]
        for b in blogs:
            blogs_data = blogSerializer(b, context={'request': request}).data
            blogs_lsit.append(blogs_data)
        return Response(matching(blogs_lsit,blog_title))




