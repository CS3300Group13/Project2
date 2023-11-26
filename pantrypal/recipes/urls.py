from django.urls import path

https://www.pacsun.com/womens/sale/?start=912from . import views

app_name = 'recipes'
urlpatterns = [
    
    path('', views.RecipeView.as_view(), name='recipes'),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),
    path('delete_recipe/<int:pk>', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    
]