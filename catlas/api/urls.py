from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import auth, post

urlpatterns = [
    # Authentication, JWT Token
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path('auth/login/', auth.LoginAPI.as_view()),
    #path('auth/register/', auth.RegistrationAPI.as_view(), name='register'),
    #path('auth/reset/', auth.ResetAPI.as_view(), name='reset'),
    #path('auth/check/', auth.CheckAPI.as_view(), name='check'),

    path('post/', post.ListAPI.as_view()),
    path('post/write/', post.CreateAPI().as_view()),
    path('post/<int:pk>/', post.GetAPI.as_view()),
    path('post/<int:pk>/update/', post.UpdateAPI.as_view()),
    path('post/<int:pk>/delete/', post.DeleteAPI.as_view())
]