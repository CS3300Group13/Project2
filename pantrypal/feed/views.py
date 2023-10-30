from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class FeedView(TemplateView):
    template_name = 'feed/feed.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass
