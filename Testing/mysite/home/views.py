from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from datetime import datetime, timedelta
from django.http import HttpResponse
from .forms import SignUpForm

User = get_user_model()
# Create your views here.

class homePage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "homepage.html", context=None)

class loginView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "userlogin.html", context=None)

    def post(self, request, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect(to="/")
        print(user)
        return render(
            request, "userlogin.html", context={"msg": "Incorrect username or password"}
        )

class signup(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "usersignup.html", context=None)

    def post(self, request, **kwargs):
        data = request.POST.copy()
        #data['contact'] = data['contact']
        data['password'] = data['password1']
        data['password2'] = data['password1']
        data['date_joined'] = datetime.now()
        data['is_active'] = True
        # print(data)
        form = SignUpForm(data)
        if form.is_valid():
            print("yes")
            form.save()
            return redirect(to = "/login/")    
        print(form.errors)
        return render(request, "usersignup.html", context={"msg": form.errors})    

class LogoutView(TemplateView):
    def get(self, request, **kwargs):
        logout(request)
        return redirect(to="/")
