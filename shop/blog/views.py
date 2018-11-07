# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post


def index(request):    
    latest_post_list = Post.objects.order_by('-published')[:5]
    # output = ', \n'.join([i.slug for i in latest_post_list])

    template = loader.get_template("index.html")
    context = { 'latest_post_list' : latest_post_list }
    return HttpResponse(template.render(context))


def detail(request, post_id):
    # try:
    #    post = Post.objects.get(pk = post_id)
    # except Post.DoesNotExist:
    #    raise Http404("Post does not exists.")

    post = get_object_or_404(Post, pk = post_id)
    template = loader.get_template("detail.html")

    context = { 'post' : post }

    return HttpResponse(template.render(context, request))
