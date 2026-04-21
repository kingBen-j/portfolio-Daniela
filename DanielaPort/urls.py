from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # API Projets
    path('api/projets/', views.api_projets_list, name='api_projets_list'),
    path('api/projets/add/', views.api_projets_add, name='api_projets_add'),
    path('api/projets/delete/<int:projet_id>/', views.api_projets_delete, name='api_projets_delete'),

    # API Stats Réseau
    path('api/stats/', views.api_stats_get, name='api_stats_get'),
    path('api/stats/update/', views.api_stats_update, name='api_stats_update'),
]