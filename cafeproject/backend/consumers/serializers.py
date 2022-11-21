from rest_framework import serializers
from .models import Profile
from django.contrib.auth.modles import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","password")
        extra_kwargs = {"password":{"write_only":True}}