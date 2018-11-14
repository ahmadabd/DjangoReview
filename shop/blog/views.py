# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-published')[:5]
    context = { 'latest_post_list' : latest_post_list }
    return render(request, 'index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    context = { 'post' : post }
    return render(request, 'detail.html', context)


def archiveYear(request, year):

    year_archive_post = get_list_or_404(Post, published__year = year)    # instead of Post.objects.filter(published__year = year)
    context = { 'year_archive_post' : year_archive_post }
    return render(request, 'archive.html', context)
