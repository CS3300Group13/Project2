from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Apps
    path('feed/', include('feed.urls', namespace='feed')),
    path('pantry/', include('pantry.urls', namespace='pantry')),
    path('users/', include('users.urls', namespace='users')),
    path('recipes/', include('recipes.urls', namespace='recipes')),
    
]
