from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import LoungeSerializer, LoungePageSerializer, LoungeDetailSerializer, LoungePageUpdateDetailView
from .models import Lounge
from django.core import serializers
from rest_framework import viewsets
from django.db.models import Q
from rest_framework import permissions
class LoungeView(viewsets.ModelViewSet):
    queryset = Lounge.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = LoungeDetailSerializer
class LoungePageView(RetrieveAPIView):
    queryset = Lounge.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = LoungeSerializer
    lookup_field = 'slug'
class LoungePageUpdateView(UpdateAPIView):
    queryset = Lounge.objects.all()
    permission_classes = (permissions.AllowAny, )
    # permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LoungePageUpdateDetailView
    lookup_field = 'slug'
class LoungeLookupView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = Lounge.objects.all()
    serializer_class = LoungeSerializer
    lookup_field = 'slug'
class SearchPage(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = LoungeSerializer
    model = serializer_class.Meta.model
    paginate_by = 5
    def get_queryset(self):
        query = self.kwargs.get('q')
        if query:
            return self.model.objects.filter(
                Q(name__icontains=query)| Q(creator__icontains=query)).distinct()
        return None

class LoungePageDetailUpdateView(UpdateAPIView):
    queryset = Lounge.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = LoungePageUpdateDetailView
    lookup_field = 'slug'
