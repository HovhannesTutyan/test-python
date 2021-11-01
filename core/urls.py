from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.contact),
    path('snipet', views.snipet_detail)
]
