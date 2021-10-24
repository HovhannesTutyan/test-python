
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_view, name="blog"),
    path('create-post/', create_post_view, name='create-post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
