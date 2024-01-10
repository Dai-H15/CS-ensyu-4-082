from django.shortcuts import render, redirect
from customUser.models import CommunityModel, CustomUserModel
# Create your views here.


def index(request):
    try:
        if request.session["is_custom_selected"] is False:
            return redirect("portal")
    except KeyError:
        return redirect("portal")
    return render(request, "chat/index.html")


def user(request):
    contexts = {}
    try:
        if request.session["is_custom_selected"] is False:
            return redirect("portal")
    except KeyError:
        return redirect("portal")
    thisuser = CustomUserModel.objects.get(custom_user_key=request.session["CustomUserKey"])
    print(thisuser.Community)
    contexts["Community"] = thisuser.Community
    users = CustomUserModel.objects.all()
    print(users)
    
    contexts["users"] = users
    if request.method == "POST":  # ユーザー検索
        if request.POST.get("username"):
            contexts["users"] = CustomUserModel.objects.filter(custom_user_Name=request.POST.get("username"))
    return render(request, "chat/user.html", contexts)


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
