from django.urls import path

from . import views
app_name='photos'
urlpatterns = [
    path('', views.photo_add_view, name='main-view'),
]
