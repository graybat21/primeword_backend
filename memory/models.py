from django.db import models

from word.models import Word


# Create your models here.


class Memory(models.Model):
    user = models.ForeignKey('auth.User')
    word = models.ForeignKey(Word)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
