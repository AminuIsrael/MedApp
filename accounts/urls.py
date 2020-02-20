from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user-registration', views.user_signup, name='user_registration'),
    path('practitioner-registration', views.practitioner_signup, name='practitioner_registration'),
    path('users/', views.UserListView.as_view(), name='users')
]