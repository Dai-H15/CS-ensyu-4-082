from django.shortcuts import render, redirect


def index(request):
    contexts = {}
    return render(request, "portal/index.html", contexts)


def firstShow(request):
    return redirect("portal")
