from django.urls import path
from . import views
app_name="core"
urlpatterns = [
    path('article/', views.article_list, name="article_list"),
    path('detail/<int:pk>/', views.article_detail, name="article_detail")
 ]