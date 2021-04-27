from rest_framework import serializers
from .models import Lounge, Videos

class LoungeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lounge
        fields = '__all__'

class LoungeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lounge
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
class LoungePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lounge
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }