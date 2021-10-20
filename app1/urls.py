from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_book/', views.saveBook, name='savebook'),
    path('getAllBooks/', views.getAllBooks,name='getAllBooks'),
    path('deletebook/', views.deleteBook, name='delete')
]