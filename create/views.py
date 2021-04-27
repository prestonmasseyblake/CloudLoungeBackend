from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import LoungeSerializer, LoungePageSerializer
from .models import Lounge
from django.core import serializers
from rest_framework import viewsets

class LoungeView(viewsets.ModelViewSet):
    queryset = Lounge.objects.all()
    serializer_class = LoungeSerializer
class LoungePageView(RetrieveAPIView):
    queryset = Lounge.objects.all()
    serializer_class = LoungeSerializer
    lookup_field = 'slug'
class LoungePageUpdateView(UpdateAPIView):
    queryset = Lounge.objects.all()
    serializer_class = LoungeSerializer
    lookup_field = 'slug'
class LoungeLookupView(viewsets.ModelViewSet):
    queryset = Lounge.objects.all()
    serializer_class = LoungeSerializer
    lookup_field = 'slug'