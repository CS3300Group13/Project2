from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from users.forms import RegistrationForm
from .models import Pal


class LoginView(TemplateView):
    template_name = 'users/login.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed:feed')
        return redirect('users:login')
    
class RegisterView(TemplateView):
    template_name = 'users/register.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('feed:feed')
        return render(request, self.template_name)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            user_profile = Pal(user=user)
            user_profile.save()
            user_profile.following.add(user_profile)
            
            return redirect('feed:feed')
        else:
            print(form.errors)
        for error in form.errors:
            print(error) 
        return redirect('users:register')
    
    
class LogoutView(TemplateView):
    
    def get(self, request):
        logout(request)
        return redirect('users:login')
    
    
class ProfileView(TemplateView):
    template_name = 'users/profile.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return render(request, self.template_name)
    
    def post(self, request):
        pass