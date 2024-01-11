from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="chat"),
    path("user/", views.user, name="chat_user"),
    path("access_chatroom/<str:distuser_key>", views.access_chatroom, name="access_chatroom"),
    path("chatroom/", views.chatroom, name="chatroom"),
    path("communities/", views.communities, name="chat_community"),
    path("access_community/<str:community_Key>", views.access_community, name="access_community"),
]
