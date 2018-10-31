# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def detail(request, post_id):
    return HttpResponse("You are looking at post {}".format(post_id))
