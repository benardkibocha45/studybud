from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from base.models import Room, Topic, Message, User
from base.forms import RoomForm, UserForm, MyUserCreationForm
from base.forms.user_forms import UserForm, MyUserCreationForm
from base.forms.room_forms import RoomForm

def topicsPage(request):
    q = request.GET.get("q") if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

