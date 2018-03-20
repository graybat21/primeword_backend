from rest_framework.serializers import ModelSerializer
from .models import Testlog


class TestlogSerializer(ModelSerializer):
    class Meta:
        model = Testlog
        fields = ('id', 'user', 'note', 'score','regdate',)
