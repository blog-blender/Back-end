from rest_framework import serializers
from .models import Post,Photo,Comment


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
