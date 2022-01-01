from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
class login(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "userlogin.html", context=None)

class signup(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "usersignup.html", context=None)
