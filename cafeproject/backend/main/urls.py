from django.urls import path, include
from main import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"menu", views.MenuViewSet)
router.register(r"event", views.EventViewSet)
router.register(r"category", views.CategoryViewSet)




urlpatterns = [
    path('', include(router.urls)),
    # path('api/',include('rest_framework', namespace="rest_framework")),
]
