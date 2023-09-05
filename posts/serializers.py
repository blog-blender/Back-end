from rest_framework import serializers
from .models import Post,Photo,Comment,Like
from accounts.models import CustomUser


class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class coment_Detail_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','profile_pic','last_name','first_name')

class postSerializer(serializers.ModelSerializer):
    Auther_id = coment_Detail_userSerializer()
    class Meta:
        model = Post
        fields = "__all__"
        # depth = 1

class commentSerializer(serializers.ModelSerializer):
    user_id = coment_Detail_userSerializer()
    class Meta:
        model = Comment
        fields = ('content','user_id','id')
        # depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user_id', 'id', 'content','post_id')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content','Auther_id','title')

class LikeSerializerforcraete(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

################################# post details costum serializers ##############
class postDetail_userSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username','profile_pic')

class postDetail_LikeSerializer(serializers.ModelSerializer):
    user_id = postDetail_userSerializer()
    class Meta:
        model = Like
        fields = "__all__"

class postDetail_CommentSerializer(serializers.ModelSerializer):
    user_id = postDetail_userSerializer()
    class Meta:
        model = Comment
        fields = ('user_id', 'content','id')

class postcreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        # depth = 1

