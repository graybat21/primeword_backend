from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from memory.models import Memory
from memory.serializers import MemorySerializer, MemoryListByUserSerializer, MemoryListByWordSerializer


class MemoryListByUser(APIView):
    """
    get: 해당 유저가 기억한 단어 리스트 전체 요청
    """

    def get(self, request, user_id):
        result = Memory.objects.filter(user=user_id)
        serializer = MemoryListByUserSerializer(result, many=True)
        return Response(serializer.data, status=200, content_type="application/json")


class MemoryListByWord(APIView):
    """
    get: 해당 단어를 기억한 user 리스트 요청
    """

    def get(self, request, word_id):
        result = Memory.objects.filter(word=word_id)
        # for i in result:
        #     data = i.user
        serializer = MemoryListByWordSerializer(result, many=True)
        return Response(serializer.data, status=200, content_type="application/json")


class MemoryListByUserAndWord(APIView):
    """
    get: 해당 유저가 기억한 단어중 하나 요청
    """

    def get(self, request, user_id, word_id):
        result = Memory.objects.filter(user=user_id, word=word_id)
        serializer = MemoryListByUserSerializer(result, many=True)
        return Response(serializer.data, status=200, content_type="application/json")


class MemoryList(ListCreateAPIView):
    """
    get: 기억한 단어들 전체 요청
    post: 기억한 단어 입력
    """
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class MemoryDetail(RetrieveUpdateDestroyAPIView):
    """
    get: 기억한 단어 요청
    put: 기억한 단어 수정
    delete: 기억한 단어 삭제
    """
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
