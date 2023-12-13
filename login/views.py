from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError


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
            contexts["res"] = 0
            return render(request, "login/createUser.html", contexts)
        except IntegrityError:
            contexts["res"] = 1
            return render(request, "login/createUser.html", contexts)
    else:
        return render(request, "login/createUser.html", contexts)


def LoginIndex(req):
    return redirect("login")
