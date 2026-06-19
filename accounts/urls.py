from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("profile/", views.ProfileAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
]
