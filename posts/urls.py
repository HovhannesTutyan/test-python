from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
     path('',views.post_list_and_create, name='main-board'),
     path('hello-world/', views.hello_world_view, name="hello-world"),
     path('data/<int:num_posts>/', views.load_post_data_view, name='data'),
     path('like-unlike/', views.like_unlike_post, name="like-unlike"),
     path('<int:pk>/', views.post_detail, name='post_detail'),
     path('<pk>/data/', views.post_detail_data_view, name='post_detail_data_view'),
     path('<pk>/update/', views.update_post, name='update_post'),
     path('<pk>/delete/', views.delete_post, name='delete_post')
]