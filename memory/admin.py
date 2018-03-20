from django.contrib import admin

from .models import Memory


class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'word', 'regdate',)
    list_display_links = list_display

admin.site.register(Memory, MemoryAdmin)