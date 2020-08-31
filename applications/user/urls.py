from django.contrib import admin
from django.urls import path

#importing the login and logout views of django 
from django.contrib.auth import views as auth_views

from . import views

#giving an app name
app_name = "user"

urlpatterns = [
    #template view 
    path('', views.HomeView.as_view(), name="home"),
    path('contact-support', views.ContactSupportView.as_view(), name="contact_support"),
    #login, logout, required login views
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name="login-required"),
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
]