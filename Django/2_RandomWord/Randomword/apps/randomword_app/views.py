# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return redirect('/random_word')

def word(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    context = {'random_word' : get_random_string(length=14)} 
    return render(request, 'randomword/index.html', context)

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word')