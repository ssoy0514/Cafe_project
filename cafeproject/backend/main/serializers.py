from rest_framework import serializers
from .models import Menu, Category, Event

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"