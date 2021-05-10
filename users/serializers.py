from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Profile

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')

class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'