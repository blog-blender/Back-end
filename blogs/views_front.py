from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import blog


class blogListView(LoginRequiredMixin, ListView):
    template_name = "blogs/blog_list.html"
    model = blog
    context_object_name = "blogs"


class blogDetailView(LoginRequiredMixin, DetailView):
    template_name = "blogs/blog_detail.html"
    model = blog


class blogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "blogs/blog_update.html"
    model = blog
    fields = "__all__"


class blogCreateView(LoginRequiredMixin, CreateView):
    template_name = "blogs/blog_create.html"
    model = blog
    fields = ["name", "rating", "reviewer"]


class blogDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "blogs/blog_delete.html"
    model = blog
    success_url = reverse_lazy("blog_list")
