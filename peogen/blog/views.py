from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from . import models


class Home(ListView):
    model = models.Post
    template_name = "blog/home.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = models.Post.objects.all().order_by("-created")[:5]
        return context
    

class PostListView(ListView):
    model = models.Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    

class PostDetailView(DetailView):
    model = models.Post
    template_name = "blog/post.html"
    context_object_name = "post"


class About(TemplateView):
    template_name = "blog/about.html"


class Contact(TemplateView):
    template_name = "blog/contact.html"

class Portfolio(TemplateView):
    template_name = "blog/portfolio.html"