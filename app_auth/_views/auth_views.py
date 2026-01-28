from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Role, Permission, RolePermission
from rest_framework import viewsets
from rest_framework import status
from .._serializers.auth_serializer import UserSerializer, GroupSerializer, RegisterSerializer, LoginSerializer, RoleSerializer, PermissionSerializer, RolePermissionSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# This class use to register user
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                #create user
                user=User.objects.create_user(
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data.get('email'),
                    password=serializer.validated_data['password'],  # hashed automatically
                    last_name=serializer.validated_data.get('last_name',""),
                    first_name=serializer.validated_data.get('first_name',"")
                )
                return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                 print("error:", e)
                 return Response(
                    {"error": "Username or email already exists."},
                    status=status.HTTP_400_BAD_REQUEST
                )    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#This class handles user login.
class LoginView(APIView):
    permission_classes =[AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message":"Login Successful.",
                    "refresh_token":str(refresh),
                    "access_token":str(refresh.access_token),
                },status = status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
