from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    
    path('', views.RecipeView.as_view(), name='recipes'),
    
]