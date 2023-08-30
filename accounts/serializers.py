from rest_framework import serializers
from accounts.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','profile_pic', 'email')


