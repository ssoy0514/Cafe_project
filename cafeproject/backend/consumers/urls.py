from django.urls import path, include
from main import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('api/',include('rest_framework', namespace="rest_framework")),
]