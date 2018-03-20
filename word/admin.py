from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin

from .models import Textbook, Note, Word

class WordResource(resources.ModelResource):
    class Meta:
        model = Word

# Register your models here.
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('textbook_id', 'name', 'grade', 'user')
    list_display_links = list_display


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_id', 'textbook', 'lesson')
    list_display_links = list_display


class WordAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('word_id', 'word', 'meaning', 'note')
    list_display_links = list_display
    resource_class = WordResource


admin.site.register(Textbook, TextbookAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Word, WordAdmin)
