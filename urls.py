from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("developer-register/",views.DeveloperRegisterView.as_view(),name="developer-register"),
    
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("manager-dashboard/",views.ManagerDashboardView.as_view(),name="manager-dashboard"),
]