from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import AuthenticatedOnly
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    """
    Generates a token that certifies the user identity.
    """
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    Register new User.
    """
    queryset = User.objects.all()
    permission_classes = [AuthenticatedOnly]
    serializer_class = RegisterSerializer


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """
    queryset = User.objects.all()
    permission_classes = [AuthenticatedOnly]
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    """
    List all users.
    """
    permission_classes = [AuthenticatedOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
