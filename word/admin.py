from django.contrib import admin
from .models import Textbook, Note, Word


# Register your models here.
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('textbook_id', 'name', 'grade', 'user')
    list_display_links = list_display


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_id', 'textbook', 'lesson')
    list_display_links = list_display


class WordAdmin(admin.ModelAdmin):
    list_display = ('word_id', 'word', 'meaning', 'note')
    list_display_links = list_display


admin.site.register(Textbook, TextbookAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Word, WordAdmin)
