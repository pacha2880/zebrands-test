from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import AuthenticatedOnly
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AuthenticatedOnly]
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AuthenticatedOnly]
    serializer_class = RegisterSerializer


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [AuthenticatedOnly]
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    permission_classes = [AuthenticatedOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
