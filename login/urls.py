from django.urls import path, include
from . import views as loginViews

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("", loginViews.LoginIndex),
    path("createUser/", loginViews.createDefUser)
]