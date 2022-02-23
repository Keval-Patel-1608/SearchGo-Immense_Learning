from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from datetime import datetime, timedelta
from django.http import HttpResponse
from matplotlib.style import context
from .forms import SignUpForm
from .models import Fields, Category, Sub_Category, Link

User = get_user_model()
class homePage(TemplateView):
        
    def get(self, request, **kwargs):
        search_word=""
        if request.method == "POST":
            search_word = request.POST['data']

    #     list1 = []
    #     if search_word != "":
    #         list1 = [{"field":"fuck","category":'you',"subcategory":'shyam'},{"field":"fuck","category":'you',"subcategory":'shyam'},{"field":"fuck","category":'you',"subcategory":'shyam'}]
    #     # book = homePage.objects.create(field='hello', category='hello', subcategory='hello')
        return render(request, "homepage.html")
    
    def post(self, request, **kwargs):
        search_word=""
        search_word = request.POST['search1']
        context = self.search(search_word)
        #print(context)
        return render(request, "homepage.html", {'context':context})
        
    def search(self, search_word):
        datasets = Sub_Category.objects.filter(Sub_Name__contains = search_word)
        context = []
        for d in datasets:
            context.append(
                {
                    "subcategory": d.Sub_Name,
                    "category": d.CategoryFK.Category_Name,
                    "fields": d.CategoryFK.FieldFK.Field_Name,
                    "links": Link.objects.filter(Sub_CategoryFK = d)
                }
            )

        print(context)
        return context
        # print(datasets)
        # for c in datasets:
        # # print(c.get('Category_FK', None))
        #     print(c.Sub_Name, c.CategoryFK.Category_Name)


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
