from django.shortcuts import render
from django.contrib.auth.models import User

def createUser(request):
    contexts = {}
    if request.method == "POST":
        password = request.POST.get("password")
        name = request.POST.get("name")
        email = request.POST.get("email")
        Newuser = User.objects.create_user(name, email, password)
        Newuser.save()
        return render 
    return render(request, "registration/createUser.html", contexts)