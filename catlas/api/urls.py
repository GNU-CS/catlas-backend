from django.urls import path, include
from knox.views import LogoutView
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(r'post', views.PostViewSet)

urlpatterns = [
    # Authentication, refactor into ViewSet
    path('auth/login/', views.LoginAPI.as_view()),
    path('auth/register/', views.RegistrationAPI.as_view()),
    path('auth/reset/', views.ResetAPI.as_view()),
    path('auth/check/', views.CheckAPI.as_view()),
    path('auth/logout/', LogoutView.as_view())
]

urlpatterns += router.urls