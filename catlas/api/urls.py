from django.urls import path, include

from knox.views import LogoutView

from api import views

urlpatterns = [
    # Authentication
    path('auth/login/', views.LoginAPI.as_view()),
    path('auth/register/', views.RegistrationAPI.as_view()),
    path('auth/reset/', views.ResetAPI.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    
    # Show data
    path('posts/', views.PostViewSet.as_view({'get': 'list'})),
    
    # Receive data
    path('upload/post/', views.CreatePostAPI.as_view())
]