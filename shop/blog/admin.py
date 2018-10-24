# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'body')
    ordering = ['status', 'published']
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Post, postAdmin)
