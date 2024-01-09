from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    try:
        if request.session["is_custom_selected"] is False:
            return redirect("portal")
    except KeyError:
        return redirect("portal")
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
