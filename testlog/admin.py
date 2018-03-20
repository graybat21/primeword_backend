from django.contrib import admin

from .models import Testlog


# Register your models here.
class TestlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'note', 'score', 'regdate',)
    list_display_links = list_display


admin.site.register(Testlog, TestlogAdmin)
