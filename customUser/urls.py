from django.urls import path, include
from . import views as CustomUserView


urlpatterns = [
    path("customuser", CustomUserView.CreateCustomUser, name="CreateCustomUser")
]
