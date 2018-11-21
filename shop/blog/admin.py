# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core import serializers
from django.contrib import admin
from .models import Post

def export_as_json(modeladmin, request, queryset):      # show posts as json
    response = HttpResponse(content_type = "application/json")
    serializers.serialize("json", queryset, stream = response)
    return response

def make_published(modeladmin, request, queryset):      # change post status to published
    result = queryset.update(status = 'published')

    if result == 1:
        message = "1 post was"
    else:
        message = "{} post was".format(result)

    modeladmin.message_user(request, "{} successfully marked as published".format(message))

def make_draft(modeladmin, request, queryset):          # change post status to draft
    result = queryset.update(status = 'draft')

    if result == 1:
        message = "1 post was"
    else:
        message = "{} post was".format(result)

    modeladmin.message_user(request, "{} successfully marked as published".format(message))


make_published.short_description = "make selected post as published"
make_draft.short_description = "make selected post as draft"
export_as_json.short_description = "Export as json"

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'body')
    ordering = ['status', 'published']
    prepopulated_fields = {'slug' : ('title',)}
    actions = [make_published, make_draft, export_as_json]

#admin.site.register(Post, postAdmin)
