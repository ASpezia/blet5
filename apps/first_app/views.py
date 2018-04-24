# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt

def register(request):
    errors = User.objects.basic_validator(request.POST)
    print "line 11"
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print errors
        return redirect("/")
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        b = User.objects.create(name=request.POST["name"], alias=request.POST["alias"],email=request.POST["email"], password=hash1)
        #above created a user, and stored it in a variable called b
        request.session["user_id"] = b.id #stored the user id in session
        request.session["alias"] = b.alias #stored the ailias in session
    return redirect("/display")

def login(request):
    errors = User.objects.login_validator(request.POST)
    print errors
    print ",,,,,"
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print errors
        return redirect("/")
    else:
        print "11111"
        user = User.objects.get(email = request.POST["email"]) #get the user based on their email. This could be any column in the User table
        request.session["user_id"] = user.id #store user id in session
        request.session["alias"] = user.alias #store alias in session
        return redirect("/display")


def index(request):
    return render(request, "index.html")

def display(request):
    return render(request,'display.html')

def somename(request, id):
    pokes = poke.objects.count(poked = request.session['user_id'])
    user = User.objects.get(id = id)
    poker = user.poked.all()
    context = {
        "user" : user,
        "poked" : User.objects.get(id = id),
        "pokes" : pokes
        }
    return render(request, 'display.html', context)

def poke(request, id):
    others = User.objects.exclude(poked = request.session['user_id'])
    user = User.objects.get(id = id) #get the user where the id matches the id of the logged user in session dictionary
    poke = User.objects.get(id = request.session['user_id']) # where the id of the poker is linked to the id of the logged in user
    poke.poked.add(user)
    context = {
        "user" : user,
        "others" : others,
        "poke" : poke
    }
    return redirect("/display", context)








def logoutfunc(request): #dome we need a seperate function and url for the logout method
    request.session.flush()
    return redirect('/logout')

def logout(request): #dome
    return render(request,'index.html')
