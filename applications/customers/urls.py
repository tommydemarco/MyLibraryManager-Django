from django.contrib import admin
from django.urls import path

from . import views

#giving an app name
app_name = "customers"

urlpatterns = [
    #list views
    path('', views.ListCustomers.as_view(), name="customers"),
    path('active-landings/', views.ListActiveLandings.as_view(), name="active_landings"),
    path('returned-landings/', views.ListReturnedLandings.as_view(), name="returned_landings"),
    #create views
    path('add-new/', views.AddNewCustomer.as_view(), name="add_new"),
    path('landings/add-new', views.AddNewLandingView.as_view(), name="add_new_landing"),
    #update views
    path('landing/returned/<pk>', views.ReturnedLanding.as_view(), name="returned_landing"),
]