from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from .forms import FormDefUser


def createDefUser(request):
    contexts = {}
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        try:
            Newuser = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            Newuser.save()
            contexts["res"] = "0"
            login(request, aut=authenticate(username=username, password=password))
            return render(request, "login/createUser.html", contexts)
        except IntegrityError:
            contexts["res"] = "1"
            return render(request, "login/createUser.html", contexts)
    else:
        contexts["form"] = FormDefUser()
    return render(request, "login/createUser.html", contexts)


def editUser(request):
    contexts = {}
    if request.method == "POST":
        password = request.POST.get("password")
        username = request.POST.get("username")
        print(username, password)
        if authenticate(username=username, password=password) is None:
            contexts["res"] = "F"
        else:
            s = User.objects.get(id=request.user.id)
            s.first_name = request.POST.get("first_name")
            s.last_name = request.POST.get("last_name")
            s.email = request.POST.get("email")
            s.save()
            contexts["res"] = "T"
    s = User.objects.get(id=request.user.id)
    contexts["username"] = s.username
    contexts["first_name"] = s.first_name
    contexts["last_name"] = s.last_name
    contexts["email"] = s.email
    return render(request, "login/editUser.html", contexts)

