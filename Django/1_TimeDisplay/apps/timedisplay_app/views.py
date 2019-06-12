# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime


# Create your views here.


def index(request):
    context = {
        
        "datetimes": strftime("%b %d, %Y", gmtime()), #this is from stackoverflow format
        "time": strftime("%I:%M %p", gmtime())

    }
    return render(request, 'index.html', context)