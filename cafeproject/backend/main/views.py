from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Menu, Category, Event
from .serializers import (
    MenuSerializer,
    CategorySerializer,
    EventSerializer
)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer