from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('follow/', views.FollowView.as_view(), name='follow'),
    path('add_friend/<int:pk>/', views.AddFriendView.as_view(), name='add_friend'),
    path('remove_friend/<int:pk>/', views.RemoveFriendView.as_view(), name='remove_friend'),
]