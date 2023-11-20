from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class RecipeView(TemplateView):
    template_name = 'recipes/recipes.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        pantry_items = PantryItem.objects.filter(pal=request.user.pal)
        context = {'pantry_items' : pantry_items}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        new_item = request.POST['item']
        new_quantity = request.POST['quantity']
        new_pantry_item = PantryItem(pal=request.user.pal, name=new_item, quantity=new_quantity)
        new_pantry_item.save()
        return redirect('pantry:pantry')
    
    
class DeleteItemView(TemplateView):
    
    def get(self, request, pk):
        PantryItem.objects.get(pk=pk).delete()
        return redirect('pantry:pantry')