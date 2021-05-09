from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from Create import models as create_models
class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')

