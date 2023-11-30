from django.urls import path, include
from . import views as loginViews

urlpatterns = [
    path("/", include('django.contrib.auth.urls')),
    path("createUser/", loginViews.createUser)
]