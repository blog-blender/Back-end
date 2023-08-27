from rest_framework import serializers
from .models import blog


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"
