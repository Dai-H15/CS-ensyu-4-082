from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import FormDefUser


def createDefUser(request):
    contexts = {}
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        Newuser = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        Newuser.save()
        contexts["res"] = "ユーザーの作成に成功しました"
        return render(request, "portal/index.html", contexts)
    else:
        contexts["form"] = FormDefUser()
    return render(request, "login/createUser.html", contexts)
