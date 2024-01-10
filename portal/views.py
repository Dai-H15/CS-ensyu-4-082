from django.shortcuts import render, redirect
from login.models import PersonalData
from customUser.models import CustomUserModel


def index(request):
    contexts = {}
    if request.user.is_authenticated:
        s = PersonalData.objects.get(user_id=request.user.id)
        if s.image:
            contexts["PersonalImage"] = s.image.url
        request.session["CustomUserKey"] = ""
        request.session["is_custom_selected"] = False
    return render(request, "portal/index.html", contexts)


def firstShow(request):
    return redirect("portal")


def redirect_app(request, to):
    contexts = {}
    if request.method == "GET":
        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            contexts["to"] = to
            contexts["customUsers"] = CustomUserModel.objects.filter(PersonalData=PersonalData.objects.get(user_id=request.user.id))
    else:
        request.session["CustomUserKey"] = request.POST.get("selectuser")
        request.session["is_custom_selected"] = True
        return redirect(request.POST.get("redirect_to"))
    return render(request, "portal/select_customuser.html", contexts)
