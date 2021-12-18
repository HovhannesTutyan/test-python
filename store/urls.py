from django.urls import path
from . import views
app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'), #first slug is the type of the variable, and second slug is the name of the variable
    path('search/<slug:category_slug>/', views.category_list, name='category_list'), # name is used to get absolute url


]