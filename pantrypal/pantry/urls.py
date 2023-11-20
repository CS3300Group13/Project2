from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'pantry'
urlpatterns = [
    
    path('', views.PantryView.as_view(), name='pantry'),
    path('delete_item/<int:pk>/', views.DeleteItemView.as_view(), name='delete_item'),
]