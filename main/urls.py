from django.urls import path
from . import views

app_name = 'ajaxapp'
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('all-articles/', views.AllArticleView, name='all_articles'),
    path('create-article/', views.CreateArticteView, name='create'),
]