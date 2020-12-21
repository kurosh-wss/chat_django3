from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models



def home(request):
    return render(request=request, template_name="blog/home.html")


class PostListView(ListView):
    model = models.Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    

class PostDetailView(DetailView):
    model = models.Post
    template_name = "blog/post.html"
    context_object_name = "post"
