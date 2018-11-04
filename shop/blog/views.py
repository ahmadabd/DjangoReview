# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse, Http404
from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-published')[:5]
    output = ', \n'.join([i.slug for i in latest_post_list])
    return HttpResponse(output)

def detail(request, post_id):
    # try:
    #    post = Post.objects.get(pk = post_id)
    # except Post.DoesNotExist:
    #    raise Http404("Post does not exists.")

    post = get_object_or_404(Post, pk = post_id)

    return HttpResponse("You are looking at post {}".format(post))
