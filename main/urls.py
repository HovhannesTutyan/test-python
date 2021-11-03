from django.urls import path

from .views import BaseView, DynamicPostsLoad

urlpatterns = [
    path('', BaseView.as_view(), name='base-view'),
    path('load-more-posts/', DynamicPostsLoad.as_view(), name='load-more-posts')
]