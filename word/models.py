from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Textbook(models.Model):
    textbook_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return str(self.pk)


class Note(models.Model):
    note_id = models.IntegerField(primary_key=True)
    textbook = models.ForeignKey(Textbook)
    lesson = models.IntegerField(default=1)

    def __str__(self):
        return str(self.pk)


class Word(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=100)
    meaning = models.TextField(max_length=500)
    note = models.ForeignKey(Note)

    def __str__(self):
        return str(self.pk)


# class User(AbstractUser):
#     school = models.CharField(max_length=100)
#     grade = models.CharField(max_length=20)
#     def __str__(self):
#         return f'{self.username}'