from django.db import models

# Create your models here.
from word.models import Note


class Testlog(models.Model):
    user = models.ForeignKey('auth.User')
    note = models.ForeignKey(Note)
    score = models.IntegerField(default=1)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
