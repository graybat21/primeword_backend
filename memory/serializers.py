from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Memory


class MemorySerializer(ModelSerializer):
    class Meta:
        model = Memory
        fields = ('id', 'user', 'word', 'regdate',)
        depth = 1


class MemoryListByUserSerializer(ModelSerializer):
    class Meta:
        model = Memory
        fields = ('id', 'word',)
        depth = 1


class MemoryListByWordSerializer(ModelSerializer):
    class Meta:
        model = Memory
        fields = ('id', 'user',)
