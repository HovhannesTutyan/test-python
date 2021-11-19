from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name='stucreate'),
    path('thanks/', views.ThanksTemplateView.as_view(extra_context={'course':'Python'}), name='thankyou'),
    path('studetail/<int:pk>', views.StudentDetailView.as_view(), name='detail'),
]
