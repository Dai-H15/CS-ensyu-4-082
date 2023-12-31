from django.urls import path
from . import views as quizViews

urlpatterns = [
    path("", quizViews.index, name="quiztop"),
    path("make", quizViews.make, name="make"),
    path("play", quizViews.play, name="play"),
    path('<int:article_id>/', quizViews.detail, name='detail'),
    path('<int:article_id>/exam', quizViews.exam, name='exam'),
    path('<int:article_id>/result', quizViews.result, name='result'),
    path('<int:article_id>/like', quizViews.like, name='like'),
    path('api/articles/<int:article_id>/like', quizViews.api_like),
    path('api/articles/<int:article_id>/result', quizViews.api_result),
]
