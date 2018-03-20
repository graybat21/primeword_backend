"""primeword_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from memory.views import MemoryList, MemoryDetail, MemoryListByUser, MemoryListByUserAndWord, MemoryListByWord
from testlog.views import TestlogList, TestlogDetail
from .api import router

schema_view = get_swagger_view(title='Primeword API')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^swagger/', schema_view),

    url(r'^memory/$', MemoryList.as_view()),
    url(r'^memory/(?P<pk>[0-9]+)/$', MemoryDetail.as_view()),
    url(r'^memory/user/(?P<user_id>[0-9]+)/$', MemoryListByUser.as_view()),
    url(r'^memory/word/(?P<word_id>[0-9]+)/$', MemoryListByWord.as_view()),
    url(r'^memory/user/(?P<user_id>[0-9]+)/word/(?P<word_id>[0-9]+)/$', MemoryListByUserAndWord.as_view()),

    url(r'^testlog/$', TestlogList.as_view()),
    url(r'^testlog/(?P<pk>[0-9]+)/$', TestlogDetail.as_view()),

    url(r'^', include(router.urls))
]
