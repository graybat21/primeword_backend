# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from testlog.models import Testlog
from testlog.serializers import TestlogSerializer


class TestlogList(ListCreateAPIView):
    """
    get: 시험기록 전체요청
    post: 시험기록 입력
    """
    queryset = Testlog.objects.all()
    serializer_class = TestlogSerializer


class TestlogDetail(RetrieveUpdateDestroyAPIView):
    """
    get: 시험 상세기록 요청
    put: 시험 상세기록 수정
    delete: 시험기록 삭제
    """
    queryset = Testlog.objects.all()
    serializer_class = TestlogSerializer
