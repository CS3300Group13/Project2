from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'users/login.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass
    
    
class LogoutView(TemplateView):
    template_name = 'users/logout.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    
class ProfileView(TemplateView):
    template_name = 'users/profile.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass
