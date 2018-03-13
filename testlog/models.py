from django.db import models
from django.utils import timezone
# Create your models here.
from word.models import Note


class Testlog(models.Model):
    user = models.ForeignKey('auth.User')
    note = models.ForeignKey(Note)
    score = models.IntegerField(default=1)
    regdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk)

