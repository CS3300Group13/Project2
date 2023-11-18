from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from.models import PantryItem


class PantryView(TemplateView):
    template_name = 'pantry/pantry.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        pantry_items = PantryItem.objects.filter(pal=request.user.pal)
        context = {'pantry_items' : pantry_items}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')