from django.contrib import admin
from .models import Textbook, Note, Word

# Register your models here.
admin.site.register(Textbook)
admin.site.register(Note)
admin.site.register(Word)