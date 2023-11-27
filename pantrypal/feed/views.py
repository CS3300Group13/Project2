from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Post
from users.models import Pal


class FeedView(TemplateView):
    template_name = 'feed/feed.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        name = request.user.first_name
        friends = request.user.pal.following.all()
        posts = Post.objects.filter(pal__in=friends)
        follow_list = request.user.pal.following.all()
        unfollowed_list = Pal.objects.exclude(following__in=follow_list)
        context = {'name' : name, 'posts' : posts, 'unfollowed_list' : unfollowed_list}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        pass
