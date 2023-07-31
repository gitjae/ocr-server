from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = [
            "username",
            "name",
            "email",
            "date_joined"
        ]
        #'__all__'

class UserJoinSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'

class UserOverviewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "name"
        ]