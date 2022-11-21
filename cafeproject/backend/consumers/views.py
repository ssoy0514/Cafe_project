from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Profile
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import (
    Serializer,
    CategorySerializer,
    EventSerializer
)

class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer
    return Response(
        {
            "user" : UserSerializer(
                user, context=self.get_serializer_context()
            ).data,
            "token" : AuthToken.objects.create(user)[1] 
        }
    )