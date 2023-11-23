from django.urls import path
from . import views as portalViews
urlpatterns = [
    path("", portalViews.firstShow),
    path("portal/", portalViews.index, name="portal")
]
