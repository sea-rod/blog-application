from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .form import CustomAddPostForm
from .models import Post


class HomePage(ListView):
    model = Post
    template_name = "home.html"


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "edit_add_post.html"
    form_class = CustomAddPostForm

    def form_valid(self, form):
        form.instance.title = form.instance.title.title()
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "detail_post.html"


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "edit_add_post.html"
    form_class = CustomAddPostForm

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user

    def form_valid(self, form):
        form.instance.title = form.instance.title.title()
        return super().form_valid(form)
