from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer, RegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


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
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            custom_user_serializer = CustomUserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': custom_user_serializer.data
            }, 200)
        else:
            return Response({"detail": "Invalid Credentials, Insert correct input"}, status=HTTP_401_UNAUTHORIZED)

# class FollowUserView(generics.APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, user_id):
#         user_to_follow = get_object_or_404(CustomUser, id=user_id)
#         request.user.following.add(user_to_follow)
#         return Response({'status': 'success', 'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

# class UnfollowUserView(generics.APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, user_id):
#         user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
#         request.user.following.remove(user_to_unfollow)
#         return Response({'status': 'success', 'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK) 
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(self.get_queryset(), id=user_id)
        request.user.following.add(user_to_follow)
        return Response({'status': 'success', 'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset =  CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(self.get_queryset(), id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'success', 'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
