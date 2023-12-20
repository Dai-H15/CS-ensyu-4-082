from django.shortcuts import render

# Create your views here.
def index(request):
    contexts = {}
    return render(request, "quiz/index.html", contexts)

def make(request):
    contexts = {}
    return render(request, "quiz/make.html", contexts)

def play(request):
    contexts = {}
    return render(request, "quiz/play.html", contexts)
