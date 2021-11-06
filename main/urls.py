from django.urls import path
from .views import main_view, game_detail_view, search_results

app_name = 'games'

urlpatterns = [
    path('', main_view, name='main'),
    path('search/', search_results, name='search'),
    path('<pk>/', game_detail_view, name='detail'),
]