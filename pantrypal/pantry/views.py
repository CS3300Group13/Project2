from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class PantryView(TemplateView):
    template_name = 'pantry/pantry.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass