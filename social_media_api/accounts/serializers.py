from .models import CustomUser, Post,Comment
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]



# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = CustomUser
#         fields = ["id", "username", "email", "password", "bio"]
#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(username=validated_data["username"], email=validated_data["email"], password=validated_data["password"])
#         return user
    


from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'password']

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            password=validated_data['password']
        )
        # Generate an authentication token for the new user
        Token.objects.create(user=user)
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
class PosrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content"]
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]

    