from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("login/", views.loginView.as_view(), name = 'login'),
    path("signup/", views.signup.as_view(), name = 'signup'),
    path("", views.homePage.as_view(), name = 'home'),
    path("logout/", views.LogoutView.as_view()),
]