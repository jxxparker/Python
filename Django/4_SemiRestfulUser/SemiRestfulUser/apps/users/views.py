# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import users

# Create your views here.
def reroute(request):
    return redirect('/users')

def index(request):
    context = { 'users': users.objects.all()}
    return render(request, 'templateusers/index.html', context)

def new(request):
    return render(request, 'templateusers/new.html')

def create(request):
    errors =  users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags='tag')
        return redirect('/users/new')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        users.objects.create(first_name= first_name, last_name=last_name, email=email)
    return redirect('/users')

def display_edit(request, number):
    if request.method == 'GET':
        context = {'user': users.objects.get(id=number)}
        return render(request, 'templateusers/user.html', context)
    elif request.method == 'POST':
        user = users.objects.get(id=number)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users')

def edit(request, number):
    context = {'user': users.objects.get(id=number)}
    return render(request, 'templateusers/update.html', context)

def destroy(request, number):
    user = users.objects.get(id=number)
    user.delete()
    return redirect('/users')