from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import PantryItemForm
from.models import PantryItem


class PantryView(TemplateView):
    template_name = 'pantry/pantry.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        form = PantryItemForm()
        pantry_items = PantryItem.objects.filter(pal=request.user.pal)
        context = {'pantry_items' : pantry_items, 'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        item = PantryItem(pal=request.user.pal)
        form = PantryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('pantry:pantry')
    
    
class DeleteItemView(TemplateView):
    
    def get(self, request, pk):
        PantryItem.objects.get(pk=pk).delete()
        return redirect('pantry:pantry')