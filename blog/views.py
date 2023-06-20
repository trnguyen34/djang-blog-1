from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import SingleObjectMixin

from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "home.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    context_object_name = "post"
    template_name = "post_new.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    context_object_name = "post"
    template_name = "post_edit.html"
    fields = ["title", "image", "body"]


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("home")

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return redirect("post_detail", pk=post.pk)
        
class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    form_class = CommentForm
    template_name = "post/comment_edit.html"
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author 

    def get_success_url(self):
        return self.object.post.get_absolute_url()
        
    def get_queryset(self):
        return Comment.objects.filter(post__pk=self.kwargs['post_pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return context

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return super().form_valid(form)
        
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "post/comment_delete.html"
    
    def get_success_url(self):
        return self.object.post.get_absolute_url()