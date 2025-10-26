from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('add/', views.add_game, name='add_game'),
    path('edit/<int:pk>/', views.edit_game, name='edit_game'),
    path('delete/<int:pk>/', views.delete_game, name='delete_game'),
    path('play/<int:pk>/', views.play_game, name='play_game'),
]
