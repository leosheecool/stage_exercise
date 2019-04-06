# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import Form_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def login_view(request):
    Form = Form_login(request.type="POST" or None)
    if Form.is_valid():
        user = Form.user
        password = Form.password
    return render(request, 'auth.html', locals())