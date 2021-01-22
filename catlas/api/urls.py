from django.urls import path, include

from knox.views import LogoutView

from api.views import LoginAPI, RegistrationAPI, ResetAPI

urlpatterns = [
    path('auth/login/', LoginAPI.as_view()),
    path('auth/register/', RegistrationAPI.as_view()),
    path('auth/reset/', ResetAPI.as_view()),
    path('auth/logout/', LogoutView.as_view())
]