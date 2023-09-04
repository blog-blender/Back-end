from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
    DestroyAPIView
)
from .models import blog,Follower,Categories,Category_associate
from .permissions import IsOwnerOrReadOnly
from .serializers import blogSerializer,followerSerializer,CategoriesSerializer,Category_associateSerializer,blogSerializer_for_create,Category_associateSerializer_for_search
from rest_framework.decorators import api_view
from rest_framework.response import Response
import difflib
from rest_framework import status
from .serializers import FollowCreateSerializer
from rest_framework.views import APIView
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

#########################################################################################




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
                blogs_data = Category_associateSerializer_for_search(b, context={'request': request}).data
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
                blogs_data = Category_associateSerializer_for_search(b, context={'request': request}).data
                blogs_lsit.append(blogs_data)
            return Response(blogs_lsit)
        blogs = blog.objects.all()
        blogs_lsit=[]
        for b in blogs:
            blogs_data = blogSerializer(b, context={'request': request}).data
            blogs_lsit.append(blogs_data)
        return Response(matching_title_only(blogs_lsit,blog_title))






#########################################################################################
@api_view(['POST'])
def CreateBlog(request):
    query_dict_dict = {}
    for key, values in request.data.lists():
        if len(values) == 1:
            query_dict_dict[key] = values[0]
        else:
            query_dict_dict[key] = values
    category_names = query_dict_dict.pop('category_name', [])
    if not isinstance(category_names, list):
        category_names = [category_names]
    blog_serializer = blogSerializer_for_create(data=query_dict_dict)
    if blog_serializer.is_valid():
        new_blog = blog_serializer.save()
    else:
        return Response({'error': blog_serializer.errors}, status=400)
    for category_name in category_names:
        category_to_ser = {'category_name': category_name, 'blog_id': str(new_blog.id)}
        cat_instance = Category_associateSerializer(data=category_to_ser)
        if cat_instance.is_valid():
            cat_instance.save()
        else:
            return Response({'error': cat_instance.errors}, status=400)
    ser_query_dict_dict = blog.objects.filter(id=new_blog.id)
    new_blog_instance = blogSerializer_for_create(ser_query_dict_dict[0]).data
    post_cats = get_associates(new_blog.id)
    new_blog_instance['categories'] = post_cats
    return Response(new_blog_instance)

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

############################################### PUT ######################################

@api_view(['PUT'])
def UpdateBlog(request):
    blog_id = request.query_params.get('blog_id')
    if not blog_id:
        return Response({'error': 'Missing blog_id parameter'}, status=400)
    try:
        current_blog = blog.objects.get(pk=blog_id)
    except blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=404)
    query_dict_dict = {}
    for key, values in request.data.lists():
        if len(values) == 1:
            query_dict_dict[key] = values[0]
        else:
            query_dict_dict[key] = values
    if not 'banner' in query_dict_dict:
        query_dict_dict['banner'] = None
    if not 'blog_pic' in query_dict_dict:
        query_dict_dict['blog_pic'] = None
    blog_serializer = blogSerializer_for_create(current_blog, data=query_dict_dict)
    if blog_serializer.is_valid():
        updated_blog = blog_serializer.save()
    else:
        return Response({'error': blog_serializer.errors}, status=400)
    Category_associate.objects.filter(blog_id= f'{updated_blog.id}').delete()
    category_names = query_dict_dict.pop('category_name', [])
    if not isinstance(category_names, list):
        category_names = [category_names]
    for category_name in category_names:
        category_to_ser = {'category_name': category_name, 'blog_id': f'{updated_blog.id}'}
        cat_instance = Category_associateSerializer(data=category_to_ser)
        if cat_instance.is_valid():
            cat_instance.save()
        else:
            return Response({'error': cat_instance.errors}, status=400)
    ser_query_dict_dict = blog.objects.filter(id=f'{updated_blog.id}')
    updated_blog_instance = blogSerializer_for_create(ser_query_dict_dict[0]).data
    post_cats = get_associates(updated_blog.id)
    updated_blog_instance['categories'] = post_cats
    return Response(updated_blog_instance)

####################################### DELETE #############################################

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

def get_associates(id):
    all_cats = Category_associate.objects.filter(blog_id=id)
    cat_ser_list = []
    for cat in all_cats:
        cat_ser = Category_associateSerializer(cat).data
        cat_ser_list.append(cat_ser)
    return cat_ser_list

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


def matching_title_only(blogs_lsit,blog_title):
    best_ratio = 0.65
    best_response = []
    for i in blogs_lsit:
        ratio = difflib.SequenceMatcher(None, i["title"], blog_title).ratio()
        if ratio > best_ratio :
            best_ratio = ratio
            best_response.append(i)
    if (best_ratio >= 0.65):

        return best_response
    else :
        return blogs_lsit #if dont find return all blogs
