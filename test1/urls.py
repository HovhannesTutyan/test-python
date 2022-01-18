from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.store, name='store'),
    path('get_data/<int:num_posts>/', views.store_get_data, name='get_data'),
    path('<int:pk>/', views.detail_view, name='checkout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)