from django import template
from django.template import RequestContext, context
from django.template.defaultfilters import last
from .models import *
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# Create your views here.


class HomeTemplateView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = "post"

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs) 
        context['post'] = Post.objects.filter(status='published').order_by('-time')[:3]
        context['category'] = Tag.objects.filter(status=True)
        return context

class NewsListView(ListView):
    model = Post
    template_name = 'main/news.html'
    context_object_name = 'post-news'

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs) 
        context['post'] = Post.objects.filter(status='published',).order_by('-time')
        context['category'] = Tag.objects.filter(status=True)
        # context['number'] = Post.objects.count() #نمایش تعداد پست ها
        return context  


class NewsDetailView(DetailView):
    model = Post
    template_name = 'main/category.html'
    context_object_name = 'category_post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Tag.objects.filter(status=True)
        return context 
        

def category(request, slug):
    category_post = Post.objects.filter(daste__slug = slug).order_by('-time')
    category_categorys = Tag.objects.filter(status = True, slug = slug)
    return render(request, 'main/category_list.html', {'slug': slug, 'category_post': category_post, 'category_categorys': category_categorys}) 



class SearchList(ListView):
    template_name = 'main/search.html'
    model = Post

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.model.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        return object_list

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs) 
        context['category'] = Tag.objects.filter(status=True)
        # context['number'] = Post.objects.count() #نمایش تعداد پست ها
        return context  


def error_404(request, exception):
    return render(request, 'main/404.html')
        
        





