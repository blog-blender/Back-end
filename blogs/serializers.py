from rest_framework import serializers
from .models import blog,Follower,Categories,Category_associate
import json


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
        depth =1

class Category_associateSerializer(serializers.ModelSerializer):

    class Meta:
        model =Category_associate
        fields = "__all__"


# class BlogSerializer(serializers.ModelSerializer):
#     categories = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), many=True)

#     class Meta:
#         model = blog
#         fields = ['id', 'title', 'owner', 'banner', 'blog_pic', 'description','categories']

#     def create(self, validated_data):

#         categories_data = validated_data.pop('categories',[])

#         blog_instance = blog.objects.create(**validated_data)
#         for category in categories_data:
#             Category_associate.objects.create(category_name=category, blog_id=blog_instance)

#         return blog_instance


# class blogse(serializers.ModelSerializer):
#     """
#     Serializer to Add ModelA together with ModelB
#     """

#     class catse(serializers.ModelSerializer):
#         class Meta:
#             model = Category_associate
#             # 'model_a_field' is a FK which will be assigned after creation of 'ModelA' model entry
#             # First entry of ModelB will have (default) fieldB3 value as True, rest as False
#             # 'field4' will be derived from its counterpart from the 'Product' model attribute
#             exclude = ['blog_id']
#             # fields = '__all__'

#     model_b = catse()

#     class Meta:
#         model = blog
#         fields = '__all__'

#     def create(self, validated_data):
#         categories_data = validated_data.pop('model_b')
#         print(categories_data["category_name"])
#         blog_instance = blog.objects.create(**validated_data)
#         Category_associate.objects.create(category_name=categories_data["category_name"], blog_id=blog_instance)
#         print(blog_instance._meta.get_fields())
#         return blog_instance



# class BlogCreateSerializer(serializers.ModelSerializer):
#     category_associate = Category_associateSerializer(write_only=True)  # Use write_only for input

#     class Meta:
#         model = blog
#         fields = ['id', 'title', 'owner', 'banner', 'blog_pic', 'description', 'category_associate']

#     def create(self, validated_data):
#         category_data = validated_data.pop('category_associate')
#         category_name = category_data.get('category_name')  # Get the existing category name

#         try:
#             category = Categories.objects.get(category_name=category_name)  # Fetch the existing category
#         except Categories.DoesNotExist:
#             raise serializers.ValidationError("Category does not exist.")  # Handle if the category doesn't exist

#         blog_instance = blog.objects.create(**validated_data)
#         Category_associate.objects.create(blog_id=blog_instance, category_name=category)
#         return blog_instance

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
