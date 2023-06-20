from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
    )

urlpatterns = [
    path('post/<uuid:post_pk>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<uuid:post_pk>/comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path("post/<uuid:pk>/comment/create/", CommentCreateView.as_view(), name="comment_create"),
    path("post/delete/<uuid:pk>", PostDeleteView.as_view(), name="post_delete"),
    path("post/edit/<uuid:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<uuid:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="home"),
]
