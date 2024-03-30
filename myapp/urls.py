# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Modified: Home page
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tracker/', views.tracker, name='tracker'),
    path('register/', views.register_user, name='register'),  # Added: Registration path
]
