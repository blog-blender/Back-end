from rest_framework import serializers
from .models import Post,Photo,Comment


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
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
        fields = ('user_id', 'id', 'content','post_id')

class CombinedSerializer(serializers.Serializer):
    model_a_data = postSerializer(source='*', read_only=True)
    model_b_data = commentSerializer(source='*', read_only=True)

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content','Auther_id','title')

