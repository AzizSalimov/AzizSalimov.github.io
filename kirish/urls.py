from django.urls import path
from .views import kirish
urlpatterns = [
    path('', kirish, name='kirish'),
    # Add more URL patterns here
]
