from django.urls import path, include
from . import views as quizViews

urlpatterns = [
    path("quiz/", quizViews.index, name="quiztop"),
    path("quiz/make", quizViews.make, name="make"),
    path("quiz/play", quizViews.play, name="play")
]
