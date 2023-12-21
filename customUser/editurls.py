from django.urls import path
from . import views as CustomUserView

urlpatterns = [
    path("customuser", CustomUserView.EditCustomUser, name="EditCustomUser"),
    path("community", CustomUserView.CreateCommunity, name="EditCommunity"),
]
