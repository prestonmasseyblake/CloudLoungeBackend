from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import LoungeSerializer, LoungePageSerializer
from .models import Lounge
from django.core import serializers
from rest_framework import viewsets
from django.db.models import Q
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
class SearchPage(ListAPIView):
    serializer_class = LoungeSerializer
    model = serializer_class.Meta.model
    paginate_by = 5
    def get_queryset(self):
        query = self.kwargs.get('q')
        if query:
            return self.model.objects.filter(
                Q(name__icontains=query)| Q(slug__icontains=query)).distinct()
        return None