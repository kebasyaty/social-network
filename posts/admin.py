# -*- coding: utf-8 -*-
from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin

from .models import Post, Comment


TokenAdmin.raw_id_fields = ('user',)


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    raw_id_fields = ('user',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_thumbnail', 'like', 'unlike',
                    'rating', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'like', 'unlike', 'rating')
    list_display_links = ('title', 'admin_thumbnail')
    raw_id_fields = ('user',)
    inlines = [CommentInline]
