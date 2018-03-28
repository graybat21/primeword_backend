from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Textbook(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User')
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    textbook = models.ForeignKey(Textbook)
    lesson = models.CharField(max_length=20)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson


class Word(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField(max_length=500)
    note = models.ForeignKey(Note)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

# class User(AbstractUser):
#     school = models.CharField(max_length=100)
#     grade = models.CharField(max_length=20)
#     def __str__(self):
#         return f'{self.username}'
