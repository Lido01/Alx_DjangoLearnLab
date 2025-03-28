from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer, RegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    # def get_queryset(self):
    #     qs = CustomUser.
    #     return super().get_queryset()
class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("passsword")
        user = authenticate(username=username, password=password)
        if username is not None:
            refresh = RefreshToken.for_user(user)

            custom_user_serializer = CustomUserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': custom_user_serializer.data
            }, 200)
        else:
            return Response({"detail": "Invalid Credentials"}, status=401)
