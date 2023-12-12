from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from . import views as loginViews

urlpatterns = [
    path("createUser/", loginViews.createDefUser, name="createUser"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editUser/', loginViews.editUser, name='editUser'),
    path('password_change/', PasswordChangeView.as_view(template_name="password_change.html", success_url=reverse_lazy("editUser")), name='passwordChange'),
    path("", include('django.contrib.auth.urls')),
]