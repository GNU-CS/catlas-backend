from django.urls import path, include
from knox.views import LogoutView
from rest_framework import routers

from api.views import auth, post

urlpatterns = [
    # Authentication, refactor into ViewSet
    path('auth/login/', auth.LoginAPI.as_view()),
    path('auth/register/', auth.RegistrationAPI.as_view()),
    path('auth/reset/', auth.ResetAPI.as_view()),
    path('auth/check/', auth.CheckAPI.as_view()),
    path('auth/logout/', LogoutView.as_view()),

    path('post/', post.ListAPI.as_view()),
    path('post/write/', post.CreateAPI().as_view()),
    path('post/<int:pk>/', post.GetAPI.as_view()),
    path('post/<int:pk>/update/', post.UpdateAPI.as_view()),
    path('post/<int:pk>/delete/', post.DeleteAPI.as_view())
]