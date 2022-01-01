from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("login/", views.login.as_view(), name = 'login'),
    path("signup/", views.signup.as_view(), name = 'signup'),
]