from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .keys import OPEN_AI_VAR
from .models import Recipe
from ..pantry.models import PantryItem


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

        import openai
        openai.api_key = OPEN_AI_VAR

        #foodItems = request.POST.get('pantry')
        grains = PantryItem.objects.filter(pal=request.user.pal, foodGroup="Grains")
        new_grains = ""
        for g in grains:
            new_grains += g.name + ", "
        if (new_grains == ""):
            grains = "None"
        else:
            grains = new_grains[:-2]

        proteins = PantryItem.objects.filter(pal=request.user.pal, foodGroup="Proteins")
        new_proteins = ""
        for g in proteins:
            new_proteins += g.name + ", "
        if (new_proteins == ""):
            proteins = "None"
        else:
            proteins = new_proteins[:-2]

        dairy = PantryItem.objects.filter(pal=request.user.pal, foodGroup="Dairy")
        new_dairy = ""
        for g in dairy:
            new_dairy += g.name + ", "
        if (new_dairy == ""):
            dairy = "None"
        else:
            dairy = new_dairy[:-2]

        fruits = PantryItem.objects.filter(pal=request.user.pal, foodGroup="Fruits")
        new_fruits = ""
        for g in fruits:
            new_fruits += g.name + ", "
        if (new_fruits == ""):
            fruits = "None"
        else:
            fruits = new_fruits[:-2]

        vegetables = PantryItem.objects.filter(pal=request.user.pal, foodGroup="Vegetables")
        new_vegetables = ""
        for g in vegetables:
            new_vegetables += g.name + ", "
        if (new_vegetables == ""):
            vegetables = "None"
        else:
            vegetables = new_vegetables[:-2]

        oils = PantryItem.objects.filter(pal=request.user.pal, foodGroup="Oils")
        new_oils = ""
        for g in oils:
            new_oils += g.name + ", "
        if (new_oils == ""):
            oils = "None"
        else:
            oils = new_oils[:-2]

        condiments = PantryItem.objects.filter(pal=request.user.pal, foodGroup="Condiments")
        new_condiments = ""
        for g in condiments:
            new_condiments += g.name + ", "
        if (new_condiments == ""):
            condiments = "None"
        else:
            condiments = new_condiments[:-2]

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

        userPrompt = f"Create a recipe using the following food items:\nGrains: f{grains}\n Proteins: f{proteins}\nDairy: f{dairy}\nFruits: f{fruits}\nVegetables: f{vegetables}\nOils: f{oils}\nCondiments: f{condiments}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": alignmentPrompt},
                {"role": "user", "content": userPrompt}
            ]
        )




        # GPT HERE
        new_recipe = Recipe(pal=request.user.pal, name='name from GPT', steps='Steps from GPT')
        new_recipe.save()
        return redirect('recipes:recipes')
