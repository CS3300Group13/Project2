from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Recipe


class RecipeView(TemplateView):
    template_name = 'recipes/recipes.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        recipes = Recipe.objects.filter(pal=request.user.pal)
        context = {'recipes' : recipes}
        return render(request, self.template_name, context)
    
    
class DeleteRecipeView(TemplateView):
    
    def get(self, request, pk):
        Recipe.objects.get(pk=pk).delete()
        return redirect('recipes:recipes')
    
    
class AddRecipeView(TemplateView):
    
    def get(self, request):
        # GPT HERE
        new_recipe = Recipe(pal=request.user.pal, name='name from GPT', steps='Steps from GPT')
        new_recipe.save()
        return redirect('recipes:recipes')
