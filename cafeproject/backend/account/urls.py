# from django.urls import path, include
# from main import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# # router.register(r"menu", views.MenuViewSet)




# urlpatterns = [
#     # path('', include(router.urls)),
#     # path('api/',include('rest_framework', namespace="rest_framework")),
# ]

# from django.urls import path, include
# from .views import HelloAPI, RegistrationAPI, LoginAPI

# urlpatterns = [
#     path("hello/", HelloAPI),
#     path("auth/register/", RegistrationAPI.as_view()),
#     path("auth/login/", LoginAPI.as_view()),
#     # path("auth/user/", UserAPI.as_view()),
# ]
from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('signup/consumer', views.ConsumerCreate.as_view()),
    path('signup/store', views.StoreCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    ]