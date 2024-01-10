from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="chat"),
    path("user/", views.user, name="chat_user"),
]
