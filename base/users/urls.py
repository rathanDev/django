from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('all/', views.get_all_users, name='get_all_users'),
]
