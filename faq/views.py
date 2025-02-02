from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the FAQ Home Page!")


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer