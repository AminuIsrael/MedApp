from django.urls import path
from . import views



urlpatterns = [
    path('update-details', views.update_profile, name='update_profile'),
    path('health_stats', views.health_statistics, name='health_statistics'),
]