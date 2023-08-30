from rest_framework import serializers
from .models import blog,Follower,Categories,Category_associate


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"
        read_only_fields = ('title',)

class followerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"
        depth=1

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model =Categories
        fields = "__all__"

class Category_associateSerializer(serializers.ModelSerializer):

    class Meta:
        model =Category_associate
        fields = "__all__"
class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('banner', 'description','blog_pic',)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if value is not None:
                setattr(instance, attr, value)
        instance.save()
        return instance

class FollowCreateSerializer(serializers.Serializer):
    blog_id = serializers.IntegerField()
    
class UnfollowSerializer(serializers.Serializer):
    blog_id = serializers.IntegerField()
