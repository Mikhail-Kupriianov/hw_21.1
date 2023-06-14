from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    paginate_by = 4
    model = Blog
    extra_context = {
        'title': 'Блоги'
    }


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        print(context_data)
        context_data['title'] = context_data['object']
        return context_data


class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content',)
    success_url = reverse_lazy('blog:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_preview', 'blog_is_publicated')
    success_url = reverse_lazy('blog:blogs')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs')
