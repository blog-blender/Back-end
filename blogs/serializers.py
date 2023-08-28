from rest_framework import serializers
from .models import blog,Follower


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"


class followerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"
