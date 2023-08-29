from rest_framework import serializers
from .models import blog,Follower,Categories,Category_associate


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"


class followerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model =Categories
        fields = "__all__"
        depth =1

class Category_associateSerializer(serializers.ModelSerializer):

    class Meta:
        model =Category_associate
        fields = "__all__"
        depth =1
