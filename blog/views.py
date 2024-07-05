from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    """ inherits from the generic.ListView class to display all posts """
    queryset = Post.objects.all()
    template_name = "post_list.html"
