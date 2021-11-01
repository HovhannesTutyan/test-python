from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='home'),
    path('/insert_student', views.InsertStudent, name='insert'),
    path('/update_all', views.update_all, name="update_all"),
    path('/delete_data', views.delete_data, name="delete_data"),
]
