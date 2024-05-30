from django.urls import path

from . import views
from django.contrib.auth import views as auth_views # Assuming your views are in a 'views.py' file in the same directory

urlpatterns = [
    path('', views.home, name='home'),  # Example pattern for the homepage
    path('about/', views.bookstore, name='bookstore'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
