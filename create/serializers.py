from rest_framework import serializers
from .models import Lounge, Videos

class LoungeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lounge
        fields = '__all__'

class LoungeYouTubeVideosSerializer(serializers.ModelSerializer):
    model = Videos
    fields = ('title')

class LoungeDetailSerializer(serializers.ModelSerializer):

    videos = LoungeYouTubeVideosSerializer(many = True, read_only=True)

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

class LoungePageUpdateDetailView(serializers.ModelSerializer):
    videos = LoungeYouTubeVideosSerializer(many = True)
    class Meta:
        model = Lounge
        fields = ('creator','name','slug','picture','isYoutube','isAmazon','isBitcoin','isTiktok','isSpotify','is_published','videos')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
    
    def create(self, validated_data):
        video_data = validated_data.pop('videos')
        lounge = Lounge.objects.create(**validated_data)
        for vid_data in video_data:
            Videos.object.create(lounge=lounge, **vid_data)
            
        return lounge
    
        