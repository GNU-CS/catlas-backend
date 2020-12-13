from django.urls import path, include

from api.views import RegistrationAPI

urlpatterns = [
    path('auth/login/', RegistrationAPI.as_view())
]