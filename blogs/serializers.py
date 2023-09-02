from rest_framework import serializers
from .models import blog,Follower,Categories,Category_associate
from accounts.models import CustomUser

class user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','profile_pic','id','first_name','last_name','email')

class followerSerializer(serializers.ModelSerializer):
    user_id = user_Serializer()
    class Meta:
        model = Follower
        fields = "__all__"
        depth=1

class Category_associateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Category_associate
        fields = "__all__"
        # depth = 1

class blogSerializer(serializers.ModelSerializer):
    owner = user_Serializer()
    class Meta:
        model = blog
        fields = "__all__"
        # read_only_fields = ('title')

class blogSerializer_for_create(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"
        # read_only_fields = ('title')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Categories
        fields = "__all__"
        depth =1


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
