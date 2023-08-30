from rest_framework import serializers
from .models import Post,Photo,Comment,Like


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['id', 'title', 'content', 'blog_id']
        fields = "__all__"
        # depth = 1


class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user_id', 'post_id', 'content')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"






