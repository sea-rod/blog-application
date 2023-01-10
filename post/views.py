from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .form import CustomAddPostForm, CommentForm
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


class PostDetailView(LoginRequiredMixin, View):
    model = Post
    template_name = "detail_post.html"

    def post(self, request, *args: str, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

    def get(self, request, *args: str, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)


class CommentGet(DetailView):
    model = Post
    template_name = "detail_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        post = self.get_object()
        return reverse_lazy("detail_post", kwargs={"pk": post.pk})


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
