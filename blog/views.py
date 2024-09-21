from django.shortcuts import render
from django.views.generic import CreateView

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body',)
