from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.response import Response
from .models import Post, Photo,Comment
from .serializers import postSerializer, photoSerializer,commentSerializer,CommentSerializer,PostUpdateSerializer,postDetail_CommentSerializer,postDetail_LikeSerializer,postcreateSerializer
from .models import Post, Photo,Comment,Like
from blogs.models import Follower
from rest_framework.decorators import api_view

################################### GET methods ######################################

@api_view(['GET'])
def postDetail(request):
    if request.method == 'GET':
        post_id = request.query_params.get('post_id')
        post = Post.objects.filter(id=post_id)
        return post_getter(request, post)

@api_view(['GET'])
def postList (request):
    if request.method == 'GET':
        blog_id = request.query_params.get('blog_id')
        if blog_id:
            post = Post.objects.filter(blog_id=blog_id)
        else:
            post = Post.objects.all()
        return post_getter(request, post)

@api_view(['GET'])
def RecentPosts (request):
    if request.method == 'GET':
        user_id = request.query_params.get('user_id')
        num_of_posts = request.query_params.get('num_of_posts')
        post = Post.objects.filter(Auther_id=user_id)
        post = post[::-1]
        post = post[:int(num_of_posts)]
        return post_getter(request, post)


@api_view(['GET'])
def homeView (request):
    if request.method == 'GET':
        post = get_queryset(request)
        return post_getter(request, post)

class commentListView(ListAPIView):
    serializer_class = commentSerializer
    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        if post_id:
            queryset = Comment.objects.filter(post_id=post_id)
        else:
            queryset = Comment.objects.all()
        return queryset

################################### post methods ######################################

@api_view(['POST'])
def CreatePost(request):
    query_dict_dict = {}
    for key, values in request.data.lists():
        if len(values) == 1:
            query_dict_dict[key] = values[0]
        else:
            query_dict_dict[key] = values
    if "photos" in query_dict_dict:
        photos_object = query_dict_dict.pop('photos')
    else:
        photos_object = None
    instanc = postcreateSerializer(data = query_dict_dict )
    if instanc.is_valid():
        current_post = instanc.save()
    else:
        errors = instanc.errors
        return Response(errors, status=400)
    if photos_object:
        if not isinstance(photos_object, list):
            photos_object = [photos_object]
        for photo in photos_object:
            photo_to_ser = {'data': photo ,'post_id':f'{current_post.id}'}
            photo_instance = photoSerializer (data = photo_to_ser )
            if photo_instance.is_valid():
                photo_instance.save()
            else:
                errors = instanc.errors
                return Response(errors, status=400)
        pj = get_images(current_post.id)
        query_dict_dict['photos'] = pj
    return Response (query_dict_dict)

class commentCreateView(CreateAPIView):
    serializer_class = CommentSerializer

####################################### put ########################

@api_view(['PUT'])
def UpdatePost(request):
    post_id = request.query_params.get('post_id')
    try:
        current_post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    query_dict_dict = {}
    for key, values in request.data.lists():
        if len(values) == 1:
            query_dict_dict[key] = values[0]
        else:
            query_dict_dict[key] = values
    post_serializer = PostUpdateSerializer(current_post, data=query_dict_dict)
    if post_serializer.is_valid():
        updated_post = post_serializer.save()
    else:
        return Response({'error': post_serializer.errors}, status=400)
    Photo.objects.filter(post_id= f'{updated_post.id}').delete()
    if 'photos' in query_dict_dict:
        photos_object = query_dict_dict.pop('photos')
        if not isinstance(photos_object, list):
            photos_object = [photos_object]
    else:
        photos_object = []
    if not isinstance(photos_object, list):
        photos_object = [photos_object]
    print(photos_object)
    for photo in photos_object:
        photo_to_ser = {'data': photo, 'post_id': f'{updated_post.id}'}
        photo_instance = photoSerializer(data=photo_to_ser)
        if photo_instance.is_valid():
            photo_instance.save()
        else:
            return Response({'error': photo_instance.errors}, status=400)
    pj = get_images(updated_post.id)
    query_dict_dict['photos'] = pj
    return Response(query_dict_dict)

class CommentUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'

################################################## services ############################################
def post_getter(request, post):
    post_list = []
    for p in post:
        post_data = postSerializer(p, context={'request': request}).data
        comments = Comment.objects.filter( post_id= p.id)
        if comments:
            comment_list = []
            for c in comments:
                comment_data = postDetail_CommentSerializer(c, context={'request': request}).data
                comment_list.append(comment_data)
            post_data['comments'] = comment_list
        else:
            post_data['comments'] = []
        photo = Photo.objects.filter(post_id=p.id)
        if photo:
            photos_list = []
            for p in photo:
                photo_data=photoSerializer(p, context={'request': request}).data
                photos_list.append(photo_data)
            post_data['photo'] = photos_list
        else:
            post_data['photo'] = []
        likes = Like.objects.filter(post_id=p.id)
        if likes:
            likes_list = []
            for l in likes :
                like_data=postDetail_LikeSerializer(l, context={'request': request}).data
                likes_list.append(like_data)
            post_data['likes'] = likes_list
        else:
            post_data['likes'] = []
        post_list.append(post_data)
    return Response(post_list)

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

def get_images(id):
    image = Photo.objects.filter(post_id = id)
    return photoSerializer(instance=image, many=True).data
