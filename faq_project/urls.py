from django.contrib import admin
from django.urls import path, include
from faq.views import home  # Import your home view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('api/', include('faq.urls')),  # API URLs
    path('', home, name='home'),  # Root URL mapped to the home view
]