
from django.urls import path
from .views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Map the root URL to the home view
]