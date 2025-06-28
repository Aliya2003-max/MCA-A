from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]

# Register your models here.
