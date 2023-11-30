from django.shortcuts import render


def createUser(request):
    contexts = {}
    return render(request, "registration/createUser.html", contexts)