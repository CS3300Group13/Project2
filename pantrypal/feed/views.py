
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Post


class FeedView(TemplateView):
    template_name = 'feed/feed.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        name = request.user.first_name
        friends = request.user.pal.following.all()
        about = request.user.pal.about
        posts = Post.objects.filter(pal__in=friends)
        context = {'name': name, 'posts': posts, 'about': about}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        pass
