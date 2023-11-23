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
        alignmentPrompt = """
        You are a food recipe generator for an app called 'pantrypal' to create delicious ideas for meals.
        You will be given a list of ingredients that a user has, and you should ONLY use these ingredients.
        The recipes should be relatively simple and interesting to make.
        
        You only give the recipes in the following format, adjusting the number of steps as necessary:
        Hi User,
        The name of the recipe is: {insert_recipe_name_here}
        Step 1: {insert_step_1_step}
        Step 2: {insert_step_2_step}
        Step 3: {insert_step_3_step}
        Step 4: {insert_step_4_step}
        Step 5: {insert_step_5_step}
        Step 6: {insert_step_6_step}
        Step 7: {insert_step_7_step}
        Final Step: Enjoy!
        """




        # GPT HERE
        new_recipe = Recipe(pal=request.user.pal, name='name from GPT', steps='Steps from GPT')
        new_recipe.save()
        return redirect('recipes:recipes')
