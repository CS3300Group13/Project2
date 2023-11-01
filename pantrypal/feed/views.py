from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class FeedView(TemplateView):
    template_name = 'feed/feed.html'
    
    def get(self, request):
        context = {"pal": request.user.pal}
        return render(request, self.template_name, context)
    
    def post(self, request):
        pass
