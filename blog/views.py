from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "posts_list.html"

# Detail view for a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"