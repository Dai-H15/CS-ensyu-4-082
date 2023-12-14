from django.shortcuts import render
from .models import CustomUserModel as CustomUser


def CreateCustomUser(request):
    contexts = {}
    s = CustomUser.objects.all()
    contexts["s"] = s
    return render(request, "customUser/create/customuser.html", contexts)
