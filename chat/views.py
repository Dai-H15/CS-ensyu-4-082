from django.shortcuts import render, redirect
from customUser.models import CommunityModel, CustomUserModel
from .models import ChatRoomModel
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
# Create your views here.


def index(request):
    request.session["chat_room_key"]=""
    try:
        if request.session["is_custom_selected"] is False:
            return redirect("portal")
    except KeyError:
        return redirect("portal")
    return render(request, "chat/index.html")


def user(request):
    request.session["chat_room_key"]=""
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


def access_chatroom(request, distuser_key):
    try:
        if request.session["is_custom_selected"] is False:
            return redirect("portal")
    except KeyError:
        return redirect("portal")
    contexts = {}
    chat_room_key = hex(int(distuser_key, 16) + int(request.session["CustomUserKey"], 16))
    request.session["chat_room_key"] = chat_room_key
    return render(request, "chat/access_chatroom.html", contexts)


def chatroom(request):
    try:
        if request.session["is_custom_selected"] is False:
            return redirect("portal")
    except KeyError:
        return redirect("portal")
    contexts = {}
    contexts["thisuser"] = CustomUserModel.objects.get(custom_user_key=request.session["CustomUserKey"])
    if ChatRoomModel.objects.filter(chat_room_key=request.session["chat_room_key"]).exists() is False:
        s = ChatRoomModel(chat_room_key=request.session["chat_room_key"], chat_data="[]")
        print("New room is created")
        s.save()
    else:
        s = ChatRoomModel.objects.get(chat_room_key=request.session["chat_room_key"])
        print("Chat room is loaded")
    if request.method == "POST":
        s = ChatRoomModel.objects.get(chat_room_key=request.session["chat_room_key"])
        chat_list = eval(s.chat_data)
        new_message = [{
            "username": request.POST.get("username"),
            "date": str(datetime.datetime.now()),
            "message": request.POST.get("message")
        }]
        chat_list += new_message
        s.chat_data = chat_list
        contexts["chat_data"] = chat_list
        contexts["chat_len"] = len(contexts["chat_data"])
        s.save()
        return render(request, "chat/room.html", contexts)
    if len(s.chat_data) > 2:
        contexts["chat_data"] = eval(s.chat_data)
        contexts["chat_len"] = len(contexts["chat_data"])
    else:
        contexts["chat_data"] = []
    return render(request, "chat/room.html", contexts)
