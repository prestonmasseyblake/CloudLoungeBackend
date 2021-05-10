from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from django.core import serializers
from rest_framework import viewsets
from .models import CustomUser, Profile
from django.db.models import Q
from rest_framework import permissions
# Create your views here.

class UsersView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer

