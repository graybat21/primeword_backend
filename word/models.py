import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Textbook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User')
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    textbook = models.ForeignKey(Textbook)
    lesson = models.CharField(max_length=20)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson


class Word(models.Model):
    spelling = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    note = models.ForeignKey(Note)
    meaning = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.spelling)

# class Wordclass(models.Model):
#     classname = models.CharField(max_length=20)
#     memo = models.TextField(blank=True)
#
#     def __str__(self):
#         return str(self.classname)
#
#
# class Wordinfo(models.Model):
#     word = models.ForeignKey(Word)
#     wordclass = models.ForeignKey(Wordclass)
#     meaning = models.TextField(max_length=500)
#     symbol = models.CharField(max_length=50)
#
#     # regdate = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.word)
