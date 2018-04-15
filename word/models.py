import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Textbook(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User')
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    textbook = models.ForeignKey(Textbook)
    lesson = models.CharField(max_length=20)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson


class Wordclass(models.Model):
    name = models.CharField(max_length=20)
    memo = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class Word(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField(max_length=500)
    note = models.ForeignKey(Note)
    regdate = models.DateTimeField(auto_now_add=True)
    wordclass = models.ForeignKey(Wordclass)

    def __str__(self):
        return str(self.pk)
