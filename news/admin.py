from django.contrib import admin
from .models import *


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content', 'author', 'created_at', 'updated_at']
    list_filter = ['author', 'created_at', 'updated_at']
    search_fields = ['title', 'short+content', 'author']
    ordering = ['-created_at', '-updated_at', 'title']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fieldsets = (
    ('General Information', {'fields': ('id', 'author', 'title', 'content')}),
    ('Timestamp', {'fields': ('created_at', 'updated_at'),}),
    )

    def short_content(self, obj):
        return f'{obj.content[:50]}...'
