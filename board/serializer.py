from rest_framework.serializers import ModelSerializer
from .models import Board
from users.serializer import UserOverviewSerializer

class BoardSerializer(ModelSerializer):
    username = UserOverviewSerializer(read_only=True)
    
    class Meta :
        model = Board
        fields = '__all__'
        # depth = 1
        # fields = [
        #     "title",
        #     "content",
        #     "username"
        # ]
        # exclude = [
        #     'updated_time'
        # ]