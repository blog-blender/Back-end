from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,


)
from .models import blog,Follower,Categories,Category_associate
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer,CategoriesSerializer,Category_associateSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import difflib
from rest_framework import status
import json
from rest_framework.views import APIView
from django.http import JsonResponse

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
    best_ratio = 0.65
    best_response = []
    for i in blogs_lsit:
        ratio = difflib.SequenceMatcher(None, i["blog_id"]["title"], blog_title).ratio()
        if ratio > best_ratio :
            best_ratio = ratio
            best_response.append(i)
    if (best_ratio >= 0.65):

        return best_response
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
            res_list = []
            for b in blogs:
                blogs_data = Category_associateSerializer(b, context={'request': request}).data
                blogs_lsit.append(blogs_data)
                #
                res_list = matching(blogs_lsit,blog_title)

            ###
            if res_list:
                return Response(res_list)
            else :


                blogs = blog.objects.all()
                all_blogs=[]
                for b in blogs:
                    blogs_data = blogSerializer(b, context={'request': request}).data
                    all_blogs.append(blogs_data)
                return Response(all_blogs)

            ###

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




# class CreateBlog(CreateAPIView):
#     serializer_class = BlogSerializer


# @api_view(['POST'])
# def CreateBlog(request):
#     serializer_class = BlogSerializer
#     return Response (serializer_class.create(request))

# class CreateBlog(APIView):
#     def post(self, request, format=None):
#         blog_data = request.data.get('blog_data')
#         blog_associate_data = request.data.get('blog_associate_data')

#         blog_serializer = blogSerializer(data=blog_data)
#         category_associate_serializer = CategoriesSerializer(data=blog_associate_data)

#         if blog_serializer.is_valid() and category_associate_serializer.is_valid():
#             blog_serializer.save()
#             category_associate_serializer.save()
#             return Response(
#                 {
#                     'blog_data': blog_serializer.data,
#                     'blog_associate_data': category_associate_serializer.data
#                 },
#                 status=status.HTTP_201_CREATED
#             )

#         return Response(
#             {
#                 'blog_data_errors': blog_serializer.errors if blog_data else None,
#                 'blog_associate_data_errors': category_associate_serializer.errors if blog_associate_data else None
#             },
#             status=status.HTTP_400_BAD_REQUEST
#         )

# class ModelACreateAPIView(CreateAPIView):
#     """
#     Create a new ModelA entry with ModelB entry
#     """
#     queryset = blog.objects.all()
#     serializer_class = blogse



# class BlogCreateAPIView(CreateAPIView):
#     queryset = blog.objects.all()
#     serializer_class = BlogCreateSerializer

# class CreateBlog(APIView):

#         def post(self, request, *args, **kwargs):
#             data = request.data
#             json_data = json.loads(request.body.decode('utf-8'))

#             title = data['title']
#             description = data['description']

#             banner = request.FILES.get('banner')
#             blog_pic = request.FILES.get('blog_pic')
#             print(banner)

#             blog.objects.create(
#                 title=title,
#                 banner=banner,
#                 blog_pic=blog_pic,
#                 description=description,
#                 owner=request.user
#             )

#             return Response(status=status.HTTP_201_CREATED)





class CreateBlog(APIView):
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

