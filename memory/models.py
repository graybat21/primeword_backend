from django.db import models

# Create your models here.
from django.utils import timezone

from word.models import Word


class Memory(models.Model):
    user = models.ForeignKey('auth.User')
    word = models.ForeignKey(Word)
    regdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk)

