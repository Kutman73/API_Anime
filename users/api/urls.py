from django.urls import path
from .api_views import *

urlpatterns = [
    path('authorization/', UserAuthorizationAPIView.as_view()),
    path('registration/', UserRegistrationAPIView.as_view())
]
