from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email', 'is_staff', 'is_active', 'date_joined']
    list_display_links = ['id', 'username']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['id', 'username', 'email']
    ordering = ['id', '-date_joined']
    readonly_fields = ['id', 'date_joined']
